import re


def clean_text(text: str) -> str:
    """
    Normalize extracted PDF text.
    """

    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()