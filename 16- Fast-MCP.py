from fastmcp import FastMCP

mcp = FastMCP("My Math MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """return sum."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """return greeting."""
    return f"Hello, {name}!"

@mcp.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """send email."""
    return f"Email sent to {to} with subject '{subject}' and body '{body}'."

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)