from sklearn.metrics.pairwise import cosine_similarity

from utils.logger import logger
from utils.exceptions import SemanticSearchError


def retrieve_relevant_chunks(
    query_embedding,
    chunk_embeddings,
    chunks,
    top_k=3
):
    try:

        logger.info(
            "Performing semantic search"
        )

        scores = cosine_similarity(
            [query_embedding],
            chunk_embeddings
        )[0]

        top_indices = (
            scores.argsort()[-top_k:][::-1]
        )

        relevant_chunks = [
            chunks[i]
            for i in top_indices
        ]

        logger.info(
            f"Retrieved {len(relevant_chunks)} chunks"
        )

        return relevant_chunks

    except Exception as e:

        raise SemanticSearchError(
            f"Semantic retrieval failed: {str(e)}"
        )