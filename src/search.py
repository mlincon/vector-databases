from typing import LiteralString

import numpy as np

from pgvector_extension.psycopg_3 import execute_search_query


def get_top3_similar_docs(
    embedding: list[float],
    query: LiteralString,
) -> list:
    """Find the most relevant content given the word embedded for a query

    Args:
        query_embedding (list[float]): embedded query
        query (LiteralString): the query to execute

    Returns:
        list containing the rows
    """
    embedding_array = np.array(embedding)

    return execute_search_query(query, (embedding_array,))
