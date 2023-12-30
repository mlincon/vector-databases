-- https://dba.stackexchange.com/q/104624
-- https://www.postgresqltutorial.com/postgresql-administration/postgresql-database-indexes-table-size/ -- noqa: LT05
SELECT
    table_catalog AS database_name,
    table_name,
    PG_SIZE_PRETTY(PG_DATABASE_SIZE(CURRENT_DATABASE())) AS database_size,
    PG_SIZE_PRETTY(table_size) AS table_size,
    PG_SIZE_PRETTY(indexes_size) AS indexes_size,
    PG_SIZE_PRETTY(total_size) AS total_size
FROM (
    SELECT
        table_catalog,
        table_name,
        PG_DATABASE_SIZE(CURRENT_DATABASE()) AS database_size,
        PG_TABLE_SIZE(table_name) AS table_size,
        PG_INDEXES_SIZE(table_name) AS indexes_size,
        PG_TOTAL_RELATION_SIZE(table_name) AS total_size
    FROM (
        SELECT
            table_catalog,
            ('"' || table_schema || '"."' || table_name || '"') AS table_name
        FROM information_schema.tables
    ) AS all_tables
    ORDER BY total_size DESC
) AS pretty_sizes;
