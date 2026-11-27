-- VietABank Customer 360 POC - DATA_GRANT (postgres)
-- Generated: 2026-11-27
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
BEGIN;

DROP TABLE IF EXISTS data_grant;
CREATE TABLE data_grant (
    username TEXT,
    role_name TEXT,
    branch_id TEXT,
    can_view_pii INTEGER,
    PRIMARY KEY (username)
);
INSERT INTO data_grant (username, role_name, branch_id, can_view_pii) VALUES
('admin_vietabank', 'HO_ADMIN', 'ALL', 1),
('rm_hn01', 'BRANCH_RM', 'HN01', 1),
('rm_hcm01', 'BRANCH_RM', 'HCM01', 1),
('analyst_c360', 'DATA_ANALYST', 'ALL', 0),
('telesales_dn01', 'BRANCH_TELESALES', 'DN01', 0);
COMMIT;
