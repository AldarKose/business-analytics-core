create table if not exists organizations (
    id bigserial primary key,
    name text not null,
    external_id text,
    created_at timestamptz not null default now()
);

create table if not exists sync_logs (
    id bigserial primary key,
    source_system text not null,
    entity_name text not null,
    status text not null,
    rows_count integer not null default 0,
    message text,
    created_at timestamptz not null default now()
);

create table if not exists products (
    id bigserial primary key,
    external_id text unique,
    code text,
    name text not null,
    product_type text,
    created_at timestamptz not null default now()
);

create table if not exists sales_documents (
    id bigserial primary key,
    external_id text unique,
    document_number text,
    document_date date,
    customer_name text,
    amount numeric(15,2) not null default 0,
    created_at timestamptz not null default now()
);

create table if not exists production_orders (
    id bigserial primary key,
    external_id text unique,
    document_number text,
    document_date date,
    product_id bigint references products(id),
    quantity numeric(15,3) not null default 0,
    status text,
    created_at timestamptz not null default now()
);

create table if not exists operation_plan (
    id bigserial primary key,
    production_order_id bigint references production_orders(id),
    operation_name text not null,
    planned_hours numeric(15,3) not null default 0,
    planned_rate numeric(15,2) not null default 0,
    planned_amount numeric(15,2) not null default 0
);

create table if not exists operation_fact (
    id bigserial primary key,
    production_order_id bigint references production_orders(id),
    operation_name text not null,
    employee_name text,
    fact_date date,
    fact_hours numeric(15,3) not null default 0,
    fact_amount numeric(15,2) not null default 0,
    comment text
);

create table if not exists material_plan (
    id bigserial primary key,
    production_order_id bigint references production_orders(id),
    material_name text not null,
    quantity numeric(15,3) not null default 0,
    amount numeric(15,2) not null default 0
);

create table if not exists material_fact (
    id bigserial primary key,
    production_order_id bigint references production_orders(id),
    material_name text not null,
    quantity numeric(15,3) not null default 0,
    amount numeric(15,2) not null default 0
);
