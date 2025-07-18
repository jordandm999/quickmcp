from starlette.applications import Starlette
from starlette.routing import Mount
from {{cookiecutter.project_name}}.mcp import mcp

import {{cookiecutter.project_name}}.tools
import {{cookiecutter.project_name}}.resources

mcp_app = mcp.http_app(path="/mcp")

app = Starlette(
    routes=[
        Mount("/", app=mcp_app),
    ],
    lifespan=mcp_app.lifespan,
)