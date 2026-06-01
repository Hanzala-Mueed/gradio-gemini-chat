from pypdf import PdfReader

from utils.logger import logger
from utils.exceptions import PDFReadError


def read_pdf(pdf_path: str) -> str:
    try:
        logger.info(f"Reading PDF: {pdf_path}")

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

        logger.info("PDF loaded successfully")

        return text

    except FileNotFoundError:
        logger.error("PDF file not found")
        raise PDFReadError(
            f"PDF file not found: {pdf_path}"
        )

    except Exception as e:
        logger.error(str(e))
        raise PDFReadError(
            f"Failed to read PDF: {str(e)}"
        )