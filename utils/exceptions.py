class PDFReadError(Exception):
    """Raised when PDF cannot be read."""
    pass


class GeminiAPIError(Exception):
    """Raised when Gemini request fails."""
    pass


class EmbeddingError(Exception):
    """Raised when embedding generation fails."""
    pass


class SemanticSearchError(Exception):
    """Raised when semantic retrieval fails."""
    pass