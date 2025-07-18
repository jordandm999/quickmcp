from {{cookiecutter.project_name}}.mcp import mcp

@mcp.resource("resource://example_resource")
def example_resource() -> dict:
    """Provides project configuration as JSON."""
    print("Registering example_resource")
    return {
        "name": "{{cookiecutter.project_name}}",
        "version": "{{cookiecutter.version}}",
        "features": ["tools", "resources"],
    }