# AWSレベル判定くん MCPサーバー版（for Cline）

AWS技術ブログの内容を分析し、レベルを判定するMCPサーバーです。

## 概要

このMCPサーバーは、AWS技術ブログの内容を分析し、以下の4つのレベルのいずれかに判定します：

- **Level 100**: AWSサービスの概要を解説するレベル
- **Level 200**: トピックの入門知識を持っていることを前提に、ベストプラクティス、サービス機能を解説するレベル
- **Level 300**: 対象のトピックの詳細を解説するレベル
- **Level 400**: 複数のサービス、アーキテクチャによる実装でテクノロジーがどのように機能するかを解説するレベル

## 環境要件

- Python 3.10以上
- MCP(Model Context Protocol)パッケージ v1.2.0以上
- Cline（VS Code拡張機能）

## インストール方法

```bash
# 依存関係のインストール
pip install -r requirements.txt
```

## 使用方法

### 1. Clineでの使用

#### 設定ファイルの編集

Clineの設定ファイルを編集して、このMCPサーバーを追加します。設定ファイルのパスは以下の通りです：

- macOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Windows: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

以下のJSON設定を追加します（既存のmcpServersオブジェクト内に追加）：

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

> **注意**: `/path/to/python3`には、システムのPythonインタプリタのフルパスを指定してください。
> macOSの場合：`/usr/bin/python3`や`/Library/Frameworks/Python.framework/Versions/3.x/bin/python3`など

#### 使い方

1. Clineを起動（または再起動）します
2. AWSブログ記事のテキストファイル（マークダウンなど）を@コマンドでClineへ入力し、レベル判定を依頼します

### 2. コマンドラインでのテスト

```bash
python aws_level_checker.py
```

StdIOインタフェースでMCPサーバーが起動します。

## トラブルシューティング

### No module named 'mcp'エラー

このエラーはmcpパッケージがPythonパスで見つからない場合に発生します。

**解決策**:
1. mcpパッケージがインストールされていることを確認
   ```bash
   pip install "mcp[cli]>=1.2.0"
   ```

2. Cline設定ファイルのenv部分にPYTHONPATHを追加
   ```json
   "env": {
     "PYTHONPATH": "/path/to/python/site-packages"
   }
   ```

### Pythonバージョンの互換性エラー

`match responder.request.root:`のようなシンタックスエラーは、Python 3.10以前のバージョンを使用している場合に発生します。

**解決策**:
1. Python 3.10以上を使用していることを確認
2. Cline設定で正しいPython実行ファイルのパスを指定

## 入力形式

AWSブログ記事のテキスト全文を入力します。テスト用のサンプルブログは`sample-blog.md`を参照してください。

## 出力形式

```
レベル: [判定したレベル (100/200/300/400)]
判定理由: [判定理由の詳細説明]
```
