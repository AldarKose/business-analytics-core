import os
import psycopg2
from psycopg2.extras import execute_values

from .schemas import ProductionOrderIn


def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        port=os.getenv("POSTGRES_PORT_INTERNAL", "5432"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )


def save_production_order(payload: ProductionOrderIn) -> dict:
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO production_orders (
                        external_id,
                        organization_id,
                        document_number,
                        document_date,
                        customer_order_external_id,
                        product_external_id,
                        product_name,
                        quantity,
                        status
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (external_id) DO UPDATE SET
                        organization_id = EXCLUDED.organization_id,
                        document_number = EXCLUDED.document_number,
                        document_date = EXCLUDED.document_date,
                        customer_order_external_id = EXCLUDED.customer_order_external_id,
                        product_external_id = EXCLUDED.product_external_id,
                        product_name = EXCLUDED.product_name,
                        quantity = EXCLUDED.quantity,
                        status = EXCLUDED.status
                    """,
                    (
                        payload.external_id,
                        payload.organization_id,
                        payload.document_number,
                        payload.document_date,
                        payload.customer_order_external_id,
                        payload.product_external_id,
                        payload.product_name,
                        payload.quantity,
                        payload.status,
                    ),
                )

                cur.execute(
                    "DELETE FROM production_operations_plan WHERE production_order_external_id = %s",
                    (payload.external_id,),
                )

                if payload.operations_plan:
                    execute_values(
                        cur,
                        """
                        INSERT INTO production_operations_plan (
                            production_order_external_id,
                            operation_external_id,
                            operation_name,
                            planned_hours,
                            planned_rate,
                            planned_amount,
                            employee_role,
                            sequence_number
                        )
                        VALUES %s
                        """,
                        [
                            (
                                payload.external_id,
                                item.operation_external_id,
                                item.operation_name,
                                item.planned_hours,
                                item.planned_rate,
                                item.planned_amount,
                                item.employee_role,
                                item.sequence_number,
                            )
                            for item in payload.operations_plan
                        ],
                    )

                cur.execute(
                    "DELETE FROM production_materials_plan WHERE production_order_external_id = %s",
                    (payload.external_id,),
                )

                if payload.materials_plan:
                    execute_values(
                        cur,
                        """
                        INSERT INTO production_materials_plan (
                            production_order_external_id,
                            material_external_id,
                            material_name,
                            planned_quantity,
                            planned_price,
                            planned_amount
                        )
                        VALUES %s
                        """,
                        [
                            (
                                payload.external_id,
                                item.material_external_id,
                                item.material_name,
                                item.planned_quantity,
                                item.planned_price,
                                item.planned_amount,
                            )
                            for item in payload.materials_plan
                        ],
                    )

        return {
            "status": "ok",
            "message": "Production order saved",
            "external_id": payload.external_id,
            "operations_plan_count": len(payload.operations_plan),
            "materials_plan_count": len(payload.materials_plan),
        }

    finally:
        conn.close()


def save_operation_fact(payload):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO production_operations_fact (
                        production_order_external_id,
                        operation_external_id,
                        operation_name,
                        employee_external_id,
                        employee_name,
                        master_external_id,
                        master_name,
                        work_date,
                        actual_hours,
                        actual_amount,
                        quantity,
                        source_document_external_id,
                        comment
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        payload.production_order_external_id,
                        payload.operation_external_id,
                        payload.operation_name,
                        payload.employee_external_id,
                        payload.employee_name,
                        payload.master_external_id,
                        payload.master_name,
                        payload.work_date,
                        payload.actual_hours,
                        payload.actual_amount,
                        payload.quantity,
                        payload.source_document_external_id,
                        payload.comment,
                    ),
                )
        return {"status": "ok", "message": "Operation fact saved"}
    finally:
        conn.close()


def save_material_fact(payload):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO production_materials_fact (
                        production_order_external_id,
                        material_external_id,
                        material_name,
                        actual_quantity,
                        actual_price,
                        actual_amount,
                        source_document_external_id
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        payload.production_order_external_id,
                        payload.material_external_id,
                        payload.material_name,
                        payload.actual_quantity,
                        payload.actual_price,
                        payload.actual_amount,
                        payload.source_document_external_id,
                    ),
                )
        return {"status": "ok", "message": "Material fact saved"}
    finally:
        conn.close()


def save_rework(payload):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO production_reworks (
                        production_order_external_id,
                        operation_name,
                        employee_external_id,
                        employee_name,
                        rework_reason,
                        rework_hours,
                        rework_material_amount,
                        rework_work_amount,
                        source_document_external_id
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        payload.production_order_external_id,
                        payload.operation_name,
                        payload.employee_external_id,
                        payload.employee_name,
                        payload.rework_reason,
                        payload.rework_hours,
                        payload.rework_material_amount,
                        payload.rework_work_amount,
                        payload.source_document_external_id,
                    ),
                )
        return {"status": "ok", "message": "Rework saved"}
    finally:
        conn.close()
