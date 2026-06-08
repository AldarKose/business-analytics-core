CREATE TABLE IF NOT EXISTS sync_logs (
    id BIGSERIAL PRIMARY KEY,
    source_name TEXT,
    entity_name TEXT,
    status TEXT,
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
