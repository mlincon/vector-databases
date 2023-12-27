-- set up schema and extension
CREATE SCHEMA IF NOT EXISTS app;

CREATE EXTENSION vector
WITH SCHEMA app;

-- disable
-- DROP EXTENSION IF EXISTS vector;

-- create a table
DROP TABLE IF EXISTS app.documents;
CREATE TABLE app.documents (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    embedding VECTOR(384) -- 384 is the vector dimension
)
;
