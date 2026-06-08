from fastapi import FastAPI

from app.modules.production.router import router as production_router

app = FastAPI(
    title="Business Analytics Core",
    version="0.1.0",
)

app.include_router(production_router)


@app.get("/health")
def health():
    return {"status": "ok"}
