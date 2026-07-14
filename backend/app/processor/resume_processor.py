from app.utils.text_cleaner import clean_text


def process_resume(text: str) -> dict:
    """
    Process extracted resume text.
    """

    cleaned = clean_text(text)

    return {
        "raw_text": cleaned
    }