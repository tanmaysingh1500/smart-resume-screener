import fitz
from fastapi import UploadFile


async def extract_text(file: UploadFile) -> str:
    """
    Extract raw text from a PDF file.

    Parameters
    ----------
    file : UploadFile

    Returns
    -------
    str
        Extracted text from every page.
    """

    pdf_bytes = await file.read()

    document = fitz.open(stream=pdf_bytes, filetype="pdf")

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    return "\n".join(pages)