from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.security import require_api_key
from app.db.session import get_db

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/summary")
def production_summary(db: Session = Depends(get_db)):
    result = db.execute(text("select count(*) from production_orders"))
    return {"production_orders_count": result.scalar_one()}
