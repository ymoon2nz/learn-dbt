\c fx dev;
CREATE SCHEMA IF NOT EXISTS FX;
CREATE SCHEMA IF NOT EXISTS ST;

CREATE TABLE IF NOT EXISTS fx.hist_capture (
    capture_id      SERIAL PRIMARY KEY,
    capture_date    DATE DEFAULT (now() at time zone 'utc'),
    capture_job     TEXT,
    capture_type    TEXT,
    capture_run     TEXT,
    capture_info    TEXT,
    capture_dump    JSON,
    updated         TIMESTAMP DEFAULT (now() at time zone 'utc')
);

drop table fx.run_log;
CREATE TABLE IF NOT EXISTS fx.run_log (
    log_id          SERIAL PRIMARY KEY,
    log_status		text,
    log_job         TEXT,
    log_info        TEXT,
    log_text        TEXT,
    log_dump        JSON,
    updated         TIMESTAMP DEFAULT (now() at time zone 'utc')
);

CREATE TABLE IF NOT EXISTS st.hist_capture (
    capture_id      SERIAL PRIMARY KEY,
    capture_date    DATE DEFAULT (now() at time zone 'utc'),
    capture_run     TEXT,
    capture_type    TEXT,
    capture_info    TEXT,
    capture_dump    JSON,
    updated         TIMESTAMP DEFAULT (now() at time zone 'utc')
);

drop table st.run_log;
CREATE TABLE IF NOT EXISTS st.run_log (
    log_id          SERIAL PRIMARY KEY,
    log_status		text,
    log_type        TEXT,
    log_info        TEXT,
    log_text        TEXT,
    log_dump        JSON,
    updated     TIMESTAMP DEFAULT (now() at time zone 'utc')
);
