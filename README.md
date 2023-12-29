# vector-databases

## ref:

Supabase example:

- https://www.youtube.com/watch?v=ibzlEQmgPPY&t=1s
- https://github.com/supabase-community/chatgpt-your-files
- https://supabase.com/docs/guides/ai (also based on pgvector and Postgres)

PgVector-Python:

- https://github.com/pgvector/pgvector-python
- https://github.com/supabase/vecs/blob/main/src/vecs/collection.py
- https://tembo.io/blog/vector-indexes-in-pgvector/ (pgvector indexes)
- https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/
- https://github.com/timescale/vector-cookbook
- https://supabase.com/docs/guides/ai/vector-columns?database-method=sql
- NOTE: psycopg is the successor to psycopg2: https://www.psycopg.org/psycopg3/docs/basic/install.html
- HNSW index:
  - https://jkatz05.com/post/postgres/pgvector-overview-0.5.0/
  - https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector
- AWS RDS Postgres support:
  - https://aws.amazon.com/about-aws/whats-new/2023/10/amazon-rds-postgresql-pgvector-hnsw-indexing/
  - https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/
  - https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html#postgresql-versions-version1313
  - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html

OpenAI Cookbooks on Vector Databases:

- https://weaviate.io/blog/distance-metrics-in-vector-search

ChromaDB:

- AWS deployment: https://docs.trychroma.com/deployment#simple-aws-deployment
- https://colab.research.google.com/drive/181Kummxd8yOyRqFu8I0aqjs2aqnOy4Fu?usp=sharing#scrollTo=6lfVmRQlepiI

Chunking (Token size):

- https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
- https://python.langchain.com/docs/modules/data_connection/document_transformers/#text-splitters
- https://www.pinecone.io/learn/chunking-strategies/
- https://python.langchain.com/docs/modules/data_connection/document_transformers/
