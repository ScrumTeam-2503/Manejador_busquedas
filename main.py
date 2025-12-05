import uvicorn
from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import views

limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("App shutting down")

def create_app():
    app = FastAPI(
        docs_url="/docs",
        openapi_url="/openapi.json",
        redoc_url=None,
        lifespan=lifespan
    )

    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)

    app.add_exception_handler(
        RateLimitExceeded,
        lambda r, e: JSONResponse(
            status_code=429,
            content={"detail": "Too many requests"}
        )
    )

    app.include_router(views.router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
