# Basic Pythonic MCP Server

This template creates a basic MCP server using Cookiecutter. Poetry can be used to install dependencies

## Features

- FastMCP server scaffolded with best practices
- Example resource and tool for easy extension
- Absolute imports for scalable, maintainable code

## Generated MCP Project Dependencies:
- FastMCP: To handle MCP
- Starlette: For streamable HTTP
- Uvicorn: For ASGI

## User Guide
1. **Generate a new project using Cookiecutter:**

   From the parent directory where you want your new project folder to appear, run:

   ```sh
   cookiecutter gh:yourusername/your-repo
   ```

   Or, if using a local path:

   ```sh
   cookiecutter /path/to/quickmcp
   ```

   Follow the prompts to fill in your project details.

2. **Install dependencies with Poetry:**

   ```sh
   cd <your_project_name>
   poetry install
   ```

3. **Run the server from the project root (parent of `src/`):**

   ```sh
   uvicorn src.<your_project_name>.server:app --reload
   ```

   > **Note:** Always run from the parent directory of `src/` to ensure absolute imports work.

4. **Access the MCP API:**
   - The server will be available at [http://localhost:8000/](http://localhost:8000/)

## Project Structure

<your_project_name>/
├── src/
│ └── <your_project_name>/
│ ├── mcp.py
│ ├── server.py
│ ├── resources/
│ │ ├── init.py
│ │ └── example_resource.py
│ └── tools/
│ ├── init.py
│ └── example_tool.py
├── pyproject.toml
├── uv.lock
└── ...

## Extending

- **Add tools:**  
  Create new tools in `src/<your_project_name>/tools` and add them to the import list in `tools/__init__.py`
- **Add resources:**  
  Create new resources in `src/<your_project_name>/resources` and add them to the import list in `resources/__init__.py`

## Development

- Use absolute imports throughout the codebase.
- Always run the server from the parent directory of `src/`.

## License

[Apache 2.0](LICENSE)