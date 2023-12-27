import pandas as pd
from costs import get_num_tokens

# Create new list with small content chunks to not hit max token limits
# Note: the maximum number of tokens for a single request is 8191
# https://openai.com/docs/api-reference/requests


def create_chunks(
    df: pd.DataFrame,
    col: str,
    token_size: int = 512,
):
    # list for chunked content and embeddings
    new_list = []
    # Split up the text into token sizes of around 512 tokens
    for i in range(len(df.index)):
        text = df["content"][i]
        # add content to the new list in chunks
        start = 0
        ideal_token_size = token_size
        # 1 token ~ 3/4 of a word
        ideal_size = int(ideal_token_size // (4 / 3))
        end = ideal_size
        # split text by spaces into words
        words = text.split()

        # remove empty spaces
        words = [x for x in words if x != " "]

        total_words = len(words)

        # calculate iterations
        chunks = total_words // ideal_size
        if total_words % ideal_size != 0:
            chunks += 1

        new_content = []
        for j in range(chunks):
            if end > total_words:
                end = total_words
            new_content = words[start:end]
            new_content_string = " ".join(new_content)
            new_content_token_len = get_num_tokens(new_content_string)
            if new_content_token_len > 0:
                new_list.append(
                    [
                        df["title"][i],
                        new_content_string,
                        df["url"][i],
                        new_content_token_len,
                    ]
                )
            start += ideal_size
            end += ideal_size


def create_chunks_old_2(
    df: pd.DataFrame,
    token_size: int = 512,
):
    # list for chunked content and embeddings
    new_list = []
    # Split up the text into token sizes of around 512 tokens
    for i in range(len(df.index)):
        text = df["content"][i]
        token_len = get_num_tokens(text)
        if token_len <= 512:
            new_list.append([df["title"][i], text, df["url"][i], token_len])
        else:
            # add content to the new list in chunks
            start = 0
            ideal_token_size = token_size
            # 1 token ~ 3/4 of a word
            ideal_size = int(ideal_token_size // (4 / 3))
            end = ideal_size
            # split text by spaces into words
            words = text.split()

            # remove empty spaces
            words = [x for x in words if x != " "]

            total_words = len(words)

            # calculate iterations
            chunks = total_words // ideal_size
            if total_words % ideal_size != 0:
                chunks += 1

            new_content = []
            for j in range(chunks):
                if end > total_words:
                    end = total_words
                new_content = words[start:end]
                new_content_string = " ".join(new_content)
                new_content_token_len = get_num_tokens(new_content_string)
                if new_content_token_len > 0:
                    new_list.append(
                        [
                            df["title"][i],
                            new_content_string,
                            df["url"][i],
                            new_content_token_len,
                        ]
                    )
                start += ideal_size
                end += ideal_size


def create_chunks_old(
    df: pd.DataFrame,
    token_size: int = 512,
):
    # list for chunked content and embeddings
    new_list = []
    # Split up the text into token sizes of around 512 tokens
    for i in range(len(df.index)):
        text = df["content"][i]
        token_len = get_num_tokens(text)
        if token_len <= 512:
            new_list.append([df["title"][i], df["content"][i], df["url"][i], token_len])
        else:
            # add content to the new list in chunks
            start = 0
            ideal_token_size = token_size
            # 1 token ~ 3/4 of a word
            ideal_size = int(ideal_token_size // (4 / 3))
            end = ideal_size
            # split text by spaces into words
            words = text.split()

            # remove empty spaces
            words = [x for x in words if x != " "]

            total_words = len(words)

            # calculate iterations
            chunks = total_words // ideal_size
            if total_words % ideal_size != 0:
                chunks += 1

            new_content = []
            for j in range(chunks):
                if end > total_words:
                    end = total_words
                new_content = words[start:end]
                new_content_string = " ".join(new_content)
                new_content_token_len = get_num_tokens(new_content_string)
                if new_content_token_len > 0:
                    new_list.append(
                        [
                            df["title"][i],
                            new_content_string,
                            df["url"][i],
                            new_content_token_len,
                        ]
                    )
                start += ideal_size
                end += ideal_size
