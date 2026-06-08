from fastapi import APIRouter

from .schemas import (
    ProductionOrderIn,
    ProductionOperationFactIn,
    ProductionMaterialFactIn,
    ProductionReworkIn,
)

from .service import (
    save_production_order,
    save_operation_fact,
    save_material_fact,
    save_rework,
)

router = APIRouter(prefix="/v1/production", tags=["production"])


@router.post("/orders")
def ingest_production_order(payload: ProductionOrderIn):
    return save_production_order(payload)


@router.post("/operations-fact")
def ingest_operation_fact(payload: ProductionOperationFactIn):
    return save_operation_fact(payload)


@router.post("/materials-fact")
def ingest_material_fact(payload: ProductionMaterialFactIn):
    return save_material_fact(payload)


@router.post("/reworks")
def ingest_rework(payload: ProductionReworkIn):
    return save_rework(payload)
