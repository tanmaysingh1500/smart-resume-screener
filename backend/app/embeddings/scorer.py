from app.embeddings.client import EmbeddingClient
from app.embeddings.similarity import calculate_similarity

from app.llm.schemas import ScreeningResult


client = EmbeddingClient()


def calculate_embedding_scores(
    result: ScreeningResult,
) -> dict:

    embedding_scores = {}

    for dimension in result.comparison_dimensions:

        job_text = result.job_description.get(
            dimension,
            "Not Mentioned",
        )

        candidate_text = result.candidate_resume.get(
            dimension,
            "Not Mentioned",
        )

        job_embedding = client.embed(job_text)

        candidate_embedding = client.embed(candidate_text)

        similarity_result = calculate_similarity(
            job_embedding,
            candidate_embedding,
        )

        embedding_scores[dimension] = {
            "cosine_similarity": round(
                similarity_result.cosine_similarity,
                4,
            ),
            "embedding_score": similarity_result.score,
        }

    return embedding_scores