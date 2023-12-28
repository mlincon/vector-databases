import os

import pandas as pd
from chunking import create_custom_chunks_for_blogs
from costs import get_total_embeddings_cost
from dotenv import find_dotenv, load_dotenv
from embeddings import get_embeddings_from_string
from openai import OpenAI

# os.chdir("/workspaces/vector-databases/pgvector/blogs/")


_ = load_dotenv(find_dotenv())
api_key = os.environ["OPENAI_API_KEY"]
openai_client = OpenAI(api_key=api_key)

# Load your CSV file into a pandas DataFrame
df = pd.read_csv("./data/blog_posts_data.csv")
df.head()

# estimated cost of embedding
get_total_embeddings_cost(df, col="content")

# chunk the contents
df_chunked = create_custom_chunks_for_blogs(df)

# create embeddings
_embeddings = "embeddings"
_content = "content"
df_chunked[_embeddings] = df[_content].apply(
    lambda x: get_embeddings_from_string(openai_client, x),
)
