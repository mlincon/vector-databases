import pandas as pd
import tiktoken


def get_total_embeddings_cost(df: pd.DataFrame, col: str) -> float:
    """Given a column of texts in a pandas dataframe, get an estimate
    of the total cost of embedding

    Args:
        df (pd.DataFrame): the dataframe
        col (str): name of the column with strings to embed

    Returns:
        float: _description_
    """
    token_length = df[col].apply(get_num_tokens)
    total_tokens = token_length.sum()
    total_cost = get_embedding_cost(total_tokens)
    return total_cost


def get_num_tokens(
    string: str,
    encoding_name: str = "cl100k_base",
) -> int:
    """
    Returns the number of tokens in a text string.

    Note: cl100k_base is the tokenizer for the models:
        - gpt-4
        - gpt-3.5-turbo
        - text-embedding-ada-002

    Links:
        - https://platform.openai.com/docs/guides/embeddings/embedding-models
        - https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
    """
    if not string:
        return 0
    encoding = tiktoken.get_encoding(encoding_name)
    # alternatively, load the encode via the model name
    # e.g. encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

    num_tokens = len(encoding.encode(string))
    return num_tokens


def get_embedding_cost(num_tokens: int) -> float:
    """
    Calculate the cost of embedding.
    Assumes we're using the text-embedding-ada-002 model.
    See https://openai.com/pricing
    Args:
        num_tokens (int): the number of tokens

    Returns:
        float: cost
    """
    return num_tokens / 1000 * 0.0001
