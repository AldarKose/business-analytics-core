CREATE TABLE IF NOT EXISTS production_orders (
    id BIGSERIAL PRIMARY KEY,
    external_id TEXT UNIQUE NOT NULL,
    organization_id BIGINT,
    document_number TEXT,
    document_date DATE,
    customer_order_external_id TEXT,
    product_external_id TEXT,
    product_name TEXT,
    quantity NUMERIC(15,3),
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS production_operations_plan (
    id BIGSERIAL PRIMARY KEY,
    production_order_external_id TEXT NOT NULL,
    operation_external_id TEXT,
    operation_name TEXT NOT NULL,
    planned_hours NUMERIC(15,3),
    planned_rate NUMERIC(15,2),
    planned_amount NUMERIC(15,2),
    employee_role TEXT,
    sequence_number INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS production_operations_fact (
    id BIGSERIAL PRIMARY KEY,
    production_order_external_id TEXT NOT NULL,
    operation_external_id TEXT,
    operation_name TEXT NOT NULL,
    employee_external_id TEXT,
    employee_name TEXT,
    master_external_id TEXT,
    master_name TEXT,
    work_date DATE,
    actual_hours NUMERIC(15,3),
    actual_amount NUMERIC(15,2),
    quantity NUMERIC(15,3),
    source_document_external_id TEXT,
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS production_materials_plan (
    id BIGSERIAL PRIMARY KEY,
    production_order_external_id TEXT NOT NULL,
    material_external_id TEXT,
    material_name TEXT NOT NULL,
    planned_quantity NUMERIC(15,3),
    planned_price NUMERIC(15,2),
    planned_amount NUMERIC(15,2),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS production_materials_fact (
    id BIGSERIAL PRIMARY KEY,
    production_order_external_id TEXT NOT NULL,
    material_external_id TEXT,
    material_name TEXT NOT NULL,
    actual_quantity NUMERIC(15,3),
    actual_price NUMERIC(15,2),
    actual_amount NUMERIC(15,2),
    source_document_external_id TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS production_reworks (
    id BIGSERIAL PRIMARY KEY,
    production_order_external_id TEXT NOT NULL,
    operation_name TEXT,
    employee_external_id TEXT,
    employee_name TEXT,
    rework_reason TEXT,
    rework_hours NUMERIC(15,3),
    rework_material_amount NUMERIC(15,2),
    rework_work_amount NUMERIC(15,2),
    source_document_external_id TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
