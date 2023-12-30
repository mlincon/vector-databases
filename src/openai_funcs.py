from openai import OpenAI
from openai.types import CreateEmbeddingResponse


def rpm_aware_embeddings(
    openai_client: OpenAI,
    text: str,
    rpm: int = 3,
    model: str = "text-embedding-ada-002",
) -> list[float]:
    # TODO: do something with rpm info
    return get_embeddings_from_string(openai_client, text, model)


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


def get_completion_from_messages(
    openai_client: OpenAI,
    messages: list,
    model: str = "gpt-3.5-turbo-0613",
    temperature: int = 0,
    max_tokens: int = 1000,
) -> str | None:
    """Helper functions to create an embedding for the user question and to
    get a completion response from an OpenAI model
    ref:
        - https://platform.openai.com/docs/api-reference/streaming
        - https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/

    Args:
        openai_client (OpenAI): an OpenAI client
        messages (list): message to sent and get completion
        model (str, optional): The GPT model to use. Defaults to "gpt-3.5-turbo-0613".
        temperature (int, optional): What sampling temperature to use, between 0 and 2. Defaults to 0.
        max_tokens (int, optional): The maximum number of [tokens](/tokenizer) that can be generated in the
            chat completion. Defaults to 1000.

    Returns:
        str: response from chatgpt
    """
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content
