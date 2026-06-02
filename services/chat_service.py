from config.prompts import SYSTEM_PROMPT
from document_loader.pdf_reader import read_pdf
from llm.gemini_client import generate_response
from utils.logger import logger

from services.document_service import DocumentService

from llm.embeddings import generate_query_embedding
from llm.semantic_search import retrieve_relevant_chunks



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

embeddings = (
    document_service
    .generate_document_embeddings()
)

logger.info(
    f"Embeddings Shape: {embeddings.shape}"
)


# pdf_text = read_pdf(PDF_PATH)
# print(pdf_text[:500])  # Print the first 500 characters of the PDF content for verification

def ask_question(user_question: str):

    try:

        logger.info(
            f"Question Received: {user_question}"
        )

        # Generate query embedding
        query_embedding = (
            generate_query_embedding(
                user_question
            )
        )

        # Retrieve most relevant chunks
        relevant_chunks = (
            retrieve_relevant_chunks(
                query_embedding,
                document_service.get_embeddings(),
                document_service.get_chunks(),
                top_k=3
            )
        )

        logger.info(
            f"Relevant Chunks Found: {len(relevant_chunks)}"
        )

        # Create context from retrieved chunks
        context = "\n\n".join(
            relevant_chunks
        )

        logger.info(
            f"Context Length: {len(context)}"
        )

        # Build RAG prompt
        final_prompt = f"""
{SYSTEM_PROMPT}

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{user_question}

Instructions:
1. Answer ONLY from the provided document context.
2. Do not make up information.
3. If the answer is not present in the context, respond with:
   "I could not find this information in the provided document."
"""

        answer = generate_response(
            final_prompt
        )

        return answer

    except Exception as e:

        logger.error(
            f"Chat Service Error: {str(e)}"
        )

        return (
            "An error occurred while "
            "processing your request."
        )

# def ask_question(user_question: str):

#     try:

#         logger.info(
#             f"Question Received: {user_question}"
#         )

#         #this send complete document to the model, which is not efficient for large documents
#         final_prompt = f"""
#         {SYSTEM_PROMPT}

#         DOCUMENT:
#         {pdf_text}

#         QUESTION:
#         {user_question}
#         """

#         answer = generate_response(final_prompt)

#         return answer

#     except Exception as e:

#         logger.error(str(e))

#         return (
#             "An error occurred while "
#             "processing your request."
#         )


