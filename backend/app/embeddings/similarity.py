import math
from dataclasses import dataclass


@dataclass
class SimilarityResult:
    cosine_similarity: float
    score: float


def calculate_similarity(
    embedding1: list[float],
    embedding2: list[float],
) -> SimilarityResult:

    if len(embedding1) != len(embedding2):
        raise ValueError("Embedding dimensions do not match.")

    dot_product = sum(
        a * b
        for a, b in zip(embedding1, embedding2)
    )

    magnitude1 = math.sqrt(sum(a * a for a in embedding1))
    magnitude2 = math.sqrt(sum(b * b for b in embedding2))

    if magnitude1 == 0 or magnitude2 == 0:
        similarity = 0.0
    else:
        similarity = dot_product / (magnitude1 * magnitude2)

    score = round(
        max(0.0, min(100.0, similarity * 100)),
        2,
    )

    return SimilarityResult(
        cosine_similarity=similarity,
        score=score,
    )