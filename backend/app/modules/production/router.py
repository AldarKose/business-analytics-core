from fastapi import APIRouter

from .schemas import ProductionOrderIn
from .service import save_production_order

router = APIRouter(prefix="/v1/production", tags=["production"])


@router.post("/orders")
def ingest_production_order(payload: ProductionOrderIn):
    return save_production_order(payload)
