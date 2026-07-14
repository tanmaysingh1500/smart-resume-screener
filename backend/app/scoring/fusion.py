from app.llm.schemas import ScreeningResult

from app.scoring.weights import (
    LLM_WEIGHT,
    EMBEDDING_WEIGHT,
)


def calculate_final_score(
    llm_result: ScreeningResult,
    embedding_scores: dict,
) -> dict:

    dimension_results = {}

    total_score = 0

    dimensions = llm_result.comparison_dimensions

    for dimension in dimensions:

        llm_score = (
            llm_result
            .llm_evaluation
            .dimension_scores[dimension]
            .score
        )

        embedding_score = (
            embedding_scores[dimension]
            ["embedding_score"]
        )

        final_score = round(
            (llm_score * LLM_WEIGHT)
            +
            (embedding_score * EMBEDDING_WEIGHT),
            2,
        )

        dimension_results[dimension] = {

            "llm_score": llm_score,

            "embedding_score": embedding_score,

            "final_score": final_score,

            "reason": (
                llm_result
                .llm_evaluation
                .dimension_scores[dimension]
                .reason
            ),
        }

        total_score += final_score

    overall_score = round(
        total_score / len(dimensions),
        2,
    )

    return {

        "overall_score": overall_score,

        "recommendation":
            llm_result.llm_evaluation.recommendation,

        "confidence":
            llm_result.llm_evaluation.confidence,

        "summary":
            llm_result.llm_evaluation.summary,

        "strengths":
            llm_result.llm_evaluation.strengths,

        "weaknesses":
            llm_result.llm_evaluation.weaknesses,

        "dimensions": dimension_results,
    }