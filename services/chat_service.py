from config.prompts import SYSTEM_PROMPT
from document_loader.pdf_reader import read_pdf
from llm.gemini_client import generate_response
from utils.logger import logger

from services.document_service import DocumentService



PDF_PATH = "docs/english2.pdf"

document_service = DocumentService(
    PDF_PATH
)

pdf_text = document_service.load_document()

chunks = (
    document_service
    .create_document_chunks()
)
logger.info(
    f"Chunks Created: {len(chunks)}"
)

logger.info(
    f"First Chunk:\n{chunks[0]}"
)


# pdf_text = read_pdf(PDF_PATH)
# print(pdf_text[:500])  # Print the first 500 characters of the PDF content for verification

def ask_question(user_question: str):

    try:

        logger.info(
            f"Question Received: {user_question}"
        )

        final_prompt = f"""
        {SYSTEM_PROMPT}

        DOCUMENT:
        {pdf_text}

        QUESTION:
        {user_question}
        """

        answer = generate_response(final_prompt)

        return answer

    except Exception as e:

        logger.error(str(e))

        return (
            "An error occurred while "
            "processing your request."
        )

