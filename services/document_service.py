from document_loader.pdf_reader import read_pdf
from utils.logger import logger


class DocumentService:

    def __init__(self, pdf_path: str):

        self.pdf_path = pdf_path

        self.document_text = ""

    def load_document(self):

        logger.info(
            "Loading document..."
        )

        self.document_text = read_pdf(
            self.pdf_path
        )

        logger.info(
            "Document loaded successfully"
        )

        return self.document_text