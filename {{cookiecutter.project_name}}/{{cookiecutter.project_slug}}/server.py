"""FastMCP server with basic search and fetch tools."""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP


# Create the MCP server
mcp = FastMCP("{{cookiecutter.project_name}}")


@mcp.tool()
def search(query: str) -> dict[str, Any]:
    """Search for information based on a query.
    
    Args:
        query: The search query string
        
    Returns:
        A dictionary containing search results
    """
    # TODO: Implement actual search functionality
    return {
        "query": query,
        "results": [
            {
                "title": f"Sample result for: {query}",
                "content": f"This is a placeholder search result for the query '{query}'.",
                "url": "https://example.com/result1",
            }
        ],
        "total_results": 1,
        "message": "This is a stub implementation. Replace with actual search logic.",
    }


@mcp.tool()
def fetch(url: str) -> dict[str, Any]:
    """Fetch content from a given URL.
    
    Args:
        url: The URL to fetch content from
        
    Returns:
        A dictionary containing the fetched content and metadata
    """
    # TODO: Implement actual fetch functionality
    return {
        "url": url,
        "content": f"This is placeholder content for URL: {url}",
        "status_code": 200,
        "content_type": "text/html",
        "content_length": 42,
        "message": "This is a stub implementation. Replace with actual fetch logic.",
    }


def main() -> None:
    """Run the MCP server with HTTP transport."""
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        path="/mcp/",
    )


if __name__ == "__main__":
    main()