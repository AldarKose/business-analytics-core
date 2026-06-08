from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.security import require_api_key
from app.db.session import get_db
from app.modules.production.routes import router as production_router

router = APIRouter()
router.include_router(production_router, prefix="/v1/production", tags=["production"])


@router.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("select 1"))
    return {"status": "ok"}


@router.get("/v1/secure-health", dependencies=[Depends(require_api_key)])
def secure_health():
    return {"status": "ok", "auth": "ok"}
