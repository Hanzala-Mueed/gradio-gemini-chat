from document_loader.pdf_reader import read_pdf
from utils.logger import logger

from document_loader.chunking import (
    create_chunks
)


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
    
    def create_document_chunks(self):

        self.chunks = create_chunks(
            self.document_text
        )

        return self.chunks