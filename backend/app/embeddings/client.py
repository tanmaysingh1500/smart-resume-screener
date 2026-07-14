import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "models/gemini-embedding-2"
API_KEY = os.getenv("GEMINI_API_KEY")


class EmbeddingClient:

    def __init__(self):

        if not API_KEY:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(
            api_key=API_KEY
        )

    def embed(self, text: str) -> list[float]:

        if not text:
            text = "Not Mentioned"

        response = self.client.models.embed_content(
            model=MODEL,
            contents=text,
        )

        return response.embeddings[0].values