from utils.logger import logger


def create_chunks(
    text: str,
    chunk_size: int = 500
):

    logger.info(
        f"Creating chunks with size {chunk_size}"
    )

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):
        chunks.append(
            text[i:i + chunk_size]
        )

    logger.info(
        f"Total chunks created: {len(chunks)}"
    )

    return chunks