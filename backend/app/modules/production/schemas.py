from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class ProductionOperationPlanIn(BaseModel):
    operation_external_id: Optional[str] = None
    operation_name: str
    planned_hours: Optional[float] = None
    planned_rate: Optional[float] = None
    planned_amount: Optional[float] = None
    employee_role: Optional[str] = None
    sequence_number: Optional[int] = None


class ProductionMaterialPlanIn(BaseModel):
    material_external_id: Optional[str] = None
    material_name: str
    planned_quantity: Optional[float] = None
    planned_price: Optional[float] = None
    planned_amount: Optional[float] = None


class ProductionOrderIn(BaseModel):
    external_id: str
    organization_id: Optional[int] = None
    document_number: Optional[str] = None
    document_date: Optional[date] = None
    customer_order_external_id: Optional[str] = None
    product_external_id: Optional[str] = None
    product_name: Optional[str] = None
    quantity: Optional[float] = None
    status: Optional[str] = None
    operations_plan: List[ProductionOperationPlanIn] = []
    materials_plan: List[ProductionMaterialPlanIn] = []
