import os

import openai
import pandas as pd
from costs import get_total_embeddings_cost

# Get openAI api key by reading local .env file
from dotenv import find_dotenv, load_dotenv

# os.chdir("/workspaces/vector-databases/pgvector/blogs/")


_ = load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load your CSV file into a pandas DataFrame
df = pd.read_csv("./data/blog_posts_data.csv")
df.head()

# estimated cost of embedding
get_total_embeddings_cost(df, col="content")
