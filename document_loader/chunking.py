from utils.logger import logger


def create_chunks(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
):

    logger.info(
        f"Creating chunks | size={chunk_size} | overlap={overlap}"
    )

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += (
            chunk_size - overlap
        )

    logger.info(
        f"Total chunks created: {len(chunks)}"
    )

    return chunks