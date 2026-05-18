from config.prompts import SYSTEM_PROMPT
from document_loader.pdf_reader import read_pdf
from llm.gemini_client import generate_response


PDF_PATH = "docs/english_lesson.pdf"


pdf_text = read_pdf(PDF_PATH)


def ask_question(user_question: str):

    final_prompt = f"""
    {SYSTEM_PROMPT}

    DOCUMENT CONTENT:
    {pdf_text}

    USER QUESTION:
    {user_question}
    """

    answer = generate_response(final_prompt)

    return answer