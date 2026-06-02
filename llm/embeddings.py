from sentence_transformers import SentenceTransformer

from utils.logger import logger
from utils.exceptions import EmbeddingError


try:
    logger.info(
        "Loading embedding model..."
    )

    embedding_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    logger.info(
        "Embedding model loaded"
    )

except Exception as e:
    raise EmbeddingError(
        f"Failed to load model: {str(e)}"
    )


def generate_embeddings(chunks: list[str]):

    try:

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks"
        )

        embeddings = embedding_model.encode(
            chunks,
            convert_to_numpy=True
        )

        logger.info(
            "Embeddings generated successfully"
        )

        return embeddings

    except Exception as e:

        raise EmbeddingError(
            f"Embedding generation failed: {str(e)}"
        )