"""FastAPI application entrypoint."""

from fastapi import FastAPI

from .routes import router as api_router


app = FastAPI(title="VisaMate API")


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    """Simple health probe."""
    return {"status": "ok"}


app.include_router(api_router)

