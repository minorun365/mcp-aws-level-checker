# AWSレベル判定くん MCPサーバー版

AWS技術ブログの内容を分析し、レベルを判定するMCPサーバーです。

大好評のうちにサービス終了となった [#AWSレベル判定くん](https://github.com/minorun365/aws-level-checker) の魂を継いでいます。

![Claude Desktopでの利用例](https://github.com/user-attachments/assets/ed5ae9a1-2e2a-46b3-976c-dec6255c07eb)

## 概要

このMCPサーバーは、AWS技術ブログの内容を分析し、以下の4つのレベルのいずれかに判定します：

- **Level 100**: AWSサービスの概要を解説するレベル
- **Level 200**: トピックの入門知識を持っていることを前提に、ベストプラクティス、サービス機能を解説するレベル
- **Level 300**: 対象のトピックの詳細を解説するレベル
- **Level 400**: 複数のサービス、アーキテクチャによる実装でテクノロジーがどのように機能するかを解説するレベル

## インストール

### `uvx`を使用する方法（推奨）

[`uv`](https://docs.astral.sh/uv/)を使用する場合、特別なインストールは不要です。[`uvx`](https://docs.astral.sh/uv/guides/tools/)を使って直接実行できます：

```bash
uvx mcp-aws-level-checker
```

### PyPI経由でインストールする方法

pip を使用してインストールすることもできます：

```bash
pip install mcp-aws-level-checker
```

インストール後は、次のコマンドで実行できます：

```bash
python -m mcp_aws_level_checker
```

## 設定方法

### Claude.app での設定

Claude の設定に以下を追加してください：

#### uvx を使用する場合

```json
"mcpServers": {
  "aws-level-checker": {
    "command": "uvx",
    "args": ["mcp-aws-level-checker"]
  }
}
```

#### pip でインストールした場合

```json
"mcpServers": {
  "aws-level-checker": {
    "command": "python",
    "args": ["-m", "mcp_aws_level_checker"]
  }
}
```

### VS Code での設定

VS Code の設定ファイルに以下を追加してください。`Ctrl + Shift + P` を押して、`Preferences: Open User Settings (JSON)` と入力することで設定ファイルを開けます。

あるいは、`.vscode/mcp.json` ファイルをワークスペースに作成することで、設定を他のユーザーと共有できます。

> `.vscode/mcp.json` ファイルを使用する場合は、`mcp` キーが必要です。

#### uvx を使用する場合

```json
{
  "mcp": {
    "servers": {
      "aws-level-checker": {
        "command": "uvx",
        "args": ["mcp-aws-level-checker"]
      }
    }
  }
}
```

#### pip でインストールした場合

```json
{
  "mcp": {
    "servers": {
      "aws-level-checker": {
        "command": "python",
        "args": ["-m", "mcp_aws_level_checker"]
      }
    }
  }
}
```

## MCPサーバー仕様

- ツール名： `analyze_aws_blog`
- 入力形式：AWSブログ記事のテキスト全文
- 出力形式：以下のとおり

```
レベル: [判定したレベル (100/200/300/400)]
判定理由: [判定理由の詳細説明]
```

## ヒント

[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)と組み合わせて使うと便利です。
