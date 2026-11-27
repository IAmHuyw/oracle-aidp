-- VietABank Customer 360 POC - LEADS (postgres)
-- Generated: 2026-11-27
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
BEGIN;

DROP TABLE IF EXISTS leads;
CREATE TABLE leads (
    lead_id TEXT,
    cif TEXT,
    full_name TEXT,
    branch_id TEXT,
    rm_name TEXT,
    product_code TEXT,
    product_name TEXT,
    action_type TEXT,
    status TEXT,
    notes TEXT,
    created_by TEXT,
    created_at TIMESTAMP,
    PRIMARY KEY (lead_id)
);
COMMIT;
