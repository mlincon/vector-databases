-- set up schema and extension
CREATE SCHEMA IF NOT EXISTS app;

-- ref: https://www.postgresql.org/docs/current/sql-createextension.html
CREATE EXTENSION IF NOT EXISTS vector;

-- create a table for blogs data from timescale tutorial
-- noqa: disable=all
DROP TABLE IF EXISTS app.blogs;
CREATE TABLE app.blogs (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    content TEXT NOT NULL,
    tokens INTEGER NOT NULL,
    embedding VECTOR(1536) -- 1536 is the vector dimension from OpenAI
)
;
-- noqa: enable=all
