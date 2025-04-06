from mcp.server.fastmcp import FastMCP

mcp = FastMCP("aws-level-checker")


@mcp.tool()
async def analyze_aws_blog(blog_text: str) -> str:
    """
    AWS技術ブログのテキストを分析し、技術レベルを判定します。
    
    Args:
        blog_text: AWS技術ブログのテキスト全文
        
    Returns:
        レベル判定結果と判定理由
    """
    
    prompt = f"""
    以下のAWS技術ブログのテキストを分析し、技術レベルを判定してください。
    
    レベル判定基準:
    - Level 100: AWS サービスの概要を解説するレベル
    - Level 200: トピックの入門知識を持っていることを前提に、ベストプラクティス、サービス機能を解説するレベル
    - Level 300: 対象のトピックの詳細を解説するレベル
    - Level 400: 複数のサービス、アーキテクチャによる実装でテクノロジーがどのように機能するかを解説するレベル
    
    分析対象テキスト:
    {blog_text}
    
    フォーマット:
    レベル: [判定したレベル (100/200/300/400)]
    判定理由: [判定理由の詳細説明]
    """
    
    return prompt


if __name__ == "__main__":
    mcp.run(transport='stdio')
