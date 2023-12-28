import os
import time

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

from chunking import create_custom_chunks_for_blogs
from costs import get_total_embeddings_cost
from embeddings import get_embeddings_from_string
from enums import RunEnvironment

# os.chdir("/workspaces/vector-databases/src/")

env = os.getenv("ENV", "local")
if env == RunEnvironment.local.value:
    _ = load_dotenv(find_dotenv(".local.env"))

api_key = os.environ["OPENAI_API_KEY"]
openai_client = OpenAI(api_key=api_key)

# Load your CSV file into a pandas DataFrame
df = pd.read_csv("../data/timescale/blog_posts_data.csv")
df.head()

# estimated cost of embedding
get_total_embeddings_cost(df, col="content")

# chunk the contents
df_chunked = create_custom_chunks_for_blogs(df)

# create embeddings
# TODO: taka account of rate limits!
# both the following attempts fail due to the free/default
# limit of 3 requests per minute (rpm)
_embeddings = "embeddings"
_content = "content"
df_chunked[_embeddings] = df[_content].apply(
    lambda x: get_embeddings_from_string(openai_client, x),
)

df_chunked[_embeddings] = ""
for i in range(len(df_chunked.index)):
    text = df[_content][i]
    time.sleep(10)
    df_chunked.at[i, _embeddings] = get_embeddings_from_string(openai_client, text)

# load embeddings
df_embed = pd.read_csv("../data/timescale/blog_data_and_embeddings.csv")
df_embed.head()
