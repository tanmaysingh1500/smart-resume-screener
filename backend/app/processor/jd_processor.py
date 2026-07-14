from app.utils.text_cleaner import clean_text


def process_job_description(text: str) -> dict:
    """
    Process extracted job description.
    """

    cleaned = clean_text(text)

    return {
        "raw_text": cleaned
    }