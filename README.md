# AWSレベル判定くん MCPサーバー版

AWS技術ブログの内容を分析し、レベルを判定するMCPサーバーです。

大好評のうちにサービス終了となった [#AWSレベル判定くん](https://github.com/minorun365/aws-level-checker) の魂を継いでいます。

![利用イメージ](https://github.com/user-attachments/assets/3fe16c5a-85ee-4eb7-a4cb-23ab202b1a7c)


## 概要

このMCPサーバーは、AWS技術ブログの内容を分析し、以下の4つのレベルのいずれかに判定します：

- **Level 100**: AWSサービスの概要を解説するレベル
- **Level 200**: トピックの入門知識を持っていることを前提に、ベストプラクティス、サービス機能を解説するレベル
- **Level 300**: 対象のトピックの詳細を解説するレベル
- **Level 400**: 複数のサービス、アーキテクチャによる実装でテクノロジーがどのように機能するかを解説するレベル


## インストール

```zsh
# このリポジトリのクローン
git clone https://github.com/minorun365/mcp-aws-level-checker
cd mcp-aws-level-checker

# 仮想環境の作成
python -m venv .venv

# 仮想環境のアクティベート
source .venv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt
```

## 使用方法

MCPクライアントの設定ファイルを以下のように更新します。

```json
{
  "mcpServers": {
    "aws-level-checker": {
      "command": "/path/to/mcp-aws-level-checker/.venv/bin/python",
      "args": ["/path/to/mcp-aws-level-checker/aws_level_checker.py"]
    }
  }
}
```

## 入力形式

AWSブログ記事のテキスト全文を入力します。

## 出力形式

```
レベル: [判定したレベル (100/200/300/400)]
判定理由: [判定理由の詳細説明]
```
