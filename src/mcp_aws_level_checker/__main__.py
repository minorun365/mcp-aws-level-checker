#!/usr/bin/env python3
"""
AWS Level Checker MCP Server
----------------------------

AWSの技術ブログのレベルを分析するMCPサーバー
"""

from .server import create_mcp_server

def main():
    """メインエントリーポイント"""
    mcp = create_mcp_server()
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
