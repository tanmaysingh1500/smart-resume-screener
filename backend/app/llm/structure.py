from app.llm.client import LLMClient
from app.llm.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from app.llm.schemas import ScreeningResult

client = LLMClient()


def structure_documents(job_description: str, resume: str) -> ScreeningResult:

    user_prompt = USER_PROMPT_TEMPLATE.format(
        job_description=job_description,
        resume=resume,
    )

    response = client.generate(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )

    return ScreeningResult.model_validate(response)