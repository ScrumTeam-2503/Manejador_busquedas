import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
import views
from models import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    #await db.set_provesi_db()
    yield
    # Shutdown (optional)
    print("App shutting down")


def create_app():
    app = FastAPI(
        docs_url="/docs",
        openapi_url="/openapi.json",
        redoc_url=None,
        lifespan=lifespan
    )

    app.include_router(views.router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
