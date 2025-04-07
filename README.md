# AWS レベル判定くん MCP サーバー版（for Cline）

AWS 技術ブログの内容を分析し、レベルを判定する MCP サーバーです。

大好評のうちにサービス終了となった [#AWS レベル判定くん](https://github.com/minorun365/aws-level-checker) の魂を継いでいます。

![利用イメージ](https://github.com/user-attachments/assets/3fe16c5a-85ee-4eb7-a4cb-23ab202b1a7c)

## 概要

この MCP サーバーは、AWS 技術ブログの内容を分析し、以下の 4 つのレベルのいずれかに判定します：

- **Level 100**: AWS サービスの概要を解説するレベル
- **Level 200**: トピックの入門知識を持っていることを前提に、ベストプラクティス、サービス機能を解説するレベル
- **Level 300**: 対象のトピックの詳細を解説するレベル
- **Level 400**: 複数のサービス、アーキテクチャによる実装でテクノロジーがどのように機能するかを解説するレベル

## 環境要件

- Python 3.10 以上
- MCP(Model Context Protocol)パッケージ v1.2.0 以上
- Cline（VS Code 拡張機能）

## インストール方法

```bash
# 依存関係のインストール
pip install -r requirements.txt
```

## 使用方法

### 1. Cline での使用

#### 設定ファイルの編集

Cline の設定ファイルを編集して、この MCP サーバーを追加します。設定ファイルのパスは以下の通りです：

- macOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Windows: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

以下の JSON 設定を追加します（既存の mcpServers オブジェクト内に追加）：

```json
{
  "mcpServers": {
    "aws-level-checker": {
      "command": "/path/to/python3",
      "args": ["/path/to/aws_level_checker.py"],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

> **注意**: `/path/to/python3`には、システムの Python インタプリタのフルパスを指定してください。
> macOS の場合：`/usr/bin/python3`や`/Library/Frameworks/Python.framework/Versions/3.x/bin/python3`など

#### 使い方

1. Cline を起動（または再起動）します
2. AWS ブログ記事のテキストファイル（マークダウンなど）を@コマンドで Cline へ入力し、レベル判定を依頼します

### 2. Claude desktop での使用

#### 環境準備

仮想環境を作成して必要なパッケージをインストールします：

```bash
# 仮想環境の作成
python -m venv .venv

# 仮想環境のアクティベート
source .venv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt
```

#### 設定ファイルの編集

Claude desktop の設定ファイルを編集して、この MCP サーバーを追加します：

```bash
# 設定ファイルを開く
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

以下の JSON 設定を追加します（ファイルが存在しない場合は新規作成）：

```json
{
  "mcpServers": {
    "aws-level-checker": {
      "command": "/path/to/.venv/bin/python3",
      "args": ["/path/to/aws_level_checker.py"],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

> **注意**: `/path/to/`の部分は、実際のプロジェクトのパスに置き換えてください。
> 例: `/Users/username/repos/mcp_project/mcp-aws-level-checker/.venv/bin/python3`

````

#### 使い方

1. Claude desktop を起動（または再起動）します
2. AWS ブログ記事のテキストを Claude desktop に入力し、レベル判定を依頼します

### 3. コマンドラインでのテスト

```bash
python aws_level_checker.py
````

StdIO インタフェースで MCP サーバーが起動します。

## トラブルシューティング

### No module named 'mcp'エラー

このエラーは mcp パッケージが Python パスで見つからない場合に発生します。

**解決策**:

1. mcp パッケージがインストールされていることを確認

   ```bash
   pip install "mcp[cli]>=1.2.0"
   ```

2. Cline 設定ファイルの env 部分に PYTHONPATH を追加
   ```json
   "env": {
     "PYTHONPATH": "/path/to/python/site-packages"
   }
   ```

### Python バージョンの互換性エラー

`match responder.request.root:`のようなシンタックスエラーは、Python 3.10 以前のバージョンを使用している場合に発生します。

**解決策**:

1. Python 3.10 以上を使用していることを確認
2. Cline 設定で正しい Python 実行ファイルのパスを指定

## 入力形式

AWS ブログ記事のテキスト全文を入力します。テスト用のサンプルブログは`sample-blog.md`を参照してください。

## 出力形式

```
レベル: [判定したレベル (100/200/300/400)]
判定理由: [判定理由の詳細説明]
```
