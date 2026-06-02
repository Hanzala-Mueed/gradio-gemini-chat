from document_loader.pdf_reader import read_pdf
from utils.logger import logger
from document_loader.chunking import create_chunks
from llm.embeddings import generate_embeddings
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

class DocumentService:

    def __init__(self, pdf_path: str):

        self.pdf_path = pdf_path
        self.document_text = ""
        self.chunks = []
        self.embeddings = None

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
            self.document_text,
            chunk_size=CHUNK_SIZE,
            overlap=CHUNK_OVERLAP
        )

        return self.chunks
    

    def generate_document_embeddings(self):

        logger.info(
            "Generating document embeddings"
        )

        self.embeddings = generate_embeddings(
            self.chunks
        )

        return self.embeddings
    
    def get_chunks(self):
        return self.chunks

    def get_embeddings(self):
        return self.embeddings