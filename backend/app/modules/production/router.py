from fastapi import APIRouter

from .schemas import ProductionOrderIn

router = APIRouter(prefix="/v1/production", tags=["production"])


@router.post("/orders")
def ingest_production_order(payload: ProductionOrderIn):
    return {
        "status": "ok",
        "message": "Production order accepted",
        "external_id": payload.external_id,
        "operations_plan_count": len(payload.operations_plan),
        "materials_plan_count": len(payload.materials_plan),
    }
