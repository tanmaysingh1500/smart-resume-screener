import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from app.llm.schemas import ScreeningResult

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL")
API_KEY = os.getenv("GEMINI_API_KEY")


class LLMClient:

    def __init__(self):
        if not API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        if not MODEL:
            raise ValueError("GEMINI_MODEL not found in environment variables.")

        self.client = genai.Client(api_key=API_KEY)

    def generate(self, system_prompt: str, user_prompt: str) -> dict:
        """
        Sends a prompt to Gemini and returns the parsed JSON response.
        """

        response = self.client.models.generate_content(
            model=MODEL,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2,
                response_mime_type="application/json",
            ),
        )

        if response.text is None:
            raise ValueError("Gemini returned an empty response.")

        print("\n" + "=" * 80)
        print("Gemini Response")
        print("=" * 80)
        print(response.text)
        print("=" * 80 + "\n")

        try:
            data = json.loads(response.text)
            return ScreeningResult.model_validate(data)

        except json.JSONDecodeError as e:
            print("Failed to parse Gemini JSON response:")
            print(response.text)
            raise e