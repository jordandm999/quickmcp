from {{cookiecutter.project_name}}.mcp import mcp

@mcp.tool
def example_tool(param1: int) -> str:
    """An example tool function"""
    return f"Received {param1}"