# AWSレベル判定くん MCPサーバー版

AWS技術ブログの内容を分析し、レベルを判定するMCPサーバーです。

公開を終了したWebアプリ「[AWSレベル判定くん](https://github.com/minorun365/aws-level-checker)」を、MCPサーバーにしたものです。

![Claude Desktopでの利用例](https://github.com/user-attachments/assets/ed5ae9a1-2e2a-46b3-976c-dec6255c07eb)

## 判定するレベル

AWS技術ブログの本文を渡すと、次の4段階のどれに当たるかを判定し、理由を添えて返します。

| レベル | 内容 |
|---|---|
| 100 | AWSサービスの概要を解説する |
| 200 | 入門知識を前提に、ベストプラクティスやサービスの機能を解説する |
| 300 | 対象トピックの詳細を解説する |
| 400 | 複数サービスを組み合わせた実装で、技術がどう動くかを解説する |

## インストール

### `uvx`を使用する方法（推奨）

[`uv`](https://docs.astral.sh/uv/)を使う場合、事前のインストールは不要です。[`uvx`](https://docs.astral.sh/uv/guides/tools/)で直接実行できます。

```bash
uvx mcp-aws-level-checker
```

### PyPI経由でインストールする方法

pip でインストールすることもできます。

```bash
pip install mcp-aws-level-checker
```

インストール後は、次のコマンドで実行できます。

```bash
python -m mcp_aws_level_checker
```

## 設定方法

### Claude.app での設定

Claude の設定に以下を追加してください。

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

VS Code の設定ファイルに以下を追加してください。`Ctrl + Shift + P` を押して、`Preferences: Open User Settings (JSON)` と入力すると設定ファイルを開けます。

あるいは、ワークスペースに `.vscode/mcp.json` ファイルを作成すると、設定を他のユーザーと共有できます。

> `.vscode/mcp.json` ファイルを使う場合は、`mcp` キーが必要です。

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

- ツール名：`analyze_aws_blog`
- 入力形式：AWSブログ記事のテキスト全文
- 出力形式：以下のとおり

```
レベル: [判定したレベル (100/200/300/400)]
判定理由: [判定理由の詳細説明]
```

## ヒント

[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)と組み合わせて使うと便利です。
