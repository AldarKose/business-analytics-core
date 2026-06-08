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


class ProductionOperationFactIn(BaseModel):
    production_order_external_id: str
    operation_external_id: Optional[str] = None
    operation_name: str
    employee_external_id: Optional[str] = None
    employee_name: Optional[str] = None
    master_external_id: Optional[str] = None
    master_name: Optional[str] = None
    work_date: Optional[date] = None
    actual_hours: Optional[float] = None
    actual_amount: Optional[float] = None
    quantity: Optional[float] = None
    source_document_external_id: Optional[str] = None
    comment: Optional[str] = None


class ProductionMaterialFactIn(BaseModel):
    production_order_external_id: str
    material_external_id: Optional[str] = None
    material_name: str
    actual_quantity: Optional[float] = None
    actual_price: Optional[float] = None
    actual_amount: Optional[float] = None
    source_document_external_id: Optional[str] = None


class ProductionReworkIn(BaseModel):
    production_order_external_id: str
    operation_name: Optional[str] = None
    employee_external_id: Optional[str] = None
    employee_name: Optional[str] = None
    rework_reason: Optional[str] = None
    rework_hours: Optional[float] = None
    rework_material_amount: Optional[float] = None
    rework_work_amount: Optional[float] = None
    source_document_external_id: Optional[str] = None
