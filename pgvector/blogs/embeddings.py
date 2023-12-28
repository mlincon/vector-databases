from openai import OpenAI
from openai.types import CreateEmbeddingResponse


def get_embeddings_from_string(
    openai_client: OpenAI,
    text: str,
    model: str = "text-embedding-ada-002",
) -> list[float]:
    """
    To get an embedding, send your text string to the embeddings API endpoint along
    with a choice of embedding model ID.
    The response will contain an embedding, which you can extract, save, and use.
    ref: https://platform.openai.com/docs/guides/embeddings/how-to-get-embeddings

    Args:
        client (OpenAI): an OpenAI client
        text (str): the text that will be embedded
        model (str, optional): Which model to use for embedding.
            Defaults to "text-embedding-ada-002".

    Returns:
        _type_: _description_
    """
    response: CreateEmbeddingResponse = openai_client.embeddings.create(
        model=model,
        input=text.replace("\n", " "),
    )
    return response.data[0].embedding
