import pandas as pd

from costs import get_num_tokens


def create_custom_chunks_for_blogs(
    df: pd.DataFrame,
    token_size: int = 512,
) -> pd.DataFrame:
    """
    Create new list with small content chunks to not hit max token limits
    Note: the maximum number of tokens for a single request is 8191
    https://openai.com/docs/api-reference/requests

    This function expects the blogs dataframe with columns: content, title, url.
    After tokenizing, if the number tokens is larger than the provided token size,
    split the text and add a new row for the splitted content with the same title and url

    Args:
        df (pd.DataFrame): the blogs dataframe
        token_size (int, optional): Preferred token sze. Defaults to 512.

    Returns:
        pd.DataFrame: a new dataframe, where the contents of each row match the
            preferred token length
    """
    _content = "content"
    _title = "title"
    _url = "url"
    _token_length = "token_length"

    # list for chunked content and embeddings
    new_list = []

    # Split up the text into token sizes of around 512 tokens
    for i in range(len(df.index)):
        text = df[_content][i]
        token_len = get_num_tokens(text)

        if token_len <= 512:
            new_list.append([df[_title][i], text, df[_url][i], token_len])

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
            for _ in range(chunks):
                if end > total_words:
                    end = total_words
                new_content = words[start:end]
                new_content_string = " ".join(new_content)
                new_content_token_len = get_num_tokens(new_content_string)
                if new_content_token_len > 0:
                    new_list.append(
                        [
                            df[_title][i],
                            new_content_string,
                            df[_url][i],
                            new_content_token_len,
                        ]
                    )
                start += ideal_size
                end += ideal_size

    df_new = pd.DataFrame(
        new_list,
        columns=[_title, _content, _url, _token_length],
    )

    return df_new
