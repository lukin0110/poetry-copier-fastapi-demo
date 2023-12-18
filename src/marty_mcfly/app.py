"""Marty McFly."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create app."""
    app = FastAPI(
        title="Marty McFly",
        description="An example of a FastAPI app that was scaffolded with Poetry Copier",
    )

    @app.get("/")
    def index() -> dict[str, str]:
        """Read root."""
        return {"msg": "Hello world"}

    return app
