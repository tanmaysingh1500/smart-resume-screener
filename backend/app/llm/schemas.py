from typing import Dict, List

from pydantic import BaseModel


class DimensionEvaluation(BaseModel):
    score: float
    reason: str


class LLMEvaluation(BaseModel):
    overall_score: float
    confidence: float

    recommendation: str
    summary: str

    dimension_scores: Dict[str, DimensionEvaluation]

    strengths: List[str]
    weaknesses: List[str]


class ScreeningResult(BaseModel):

    comparison_dimensions: List[str]

    job_description: Dict[str, str]

    candidate_resume: Dict[str, str]

    llm_evaluation: LLMEvaluation