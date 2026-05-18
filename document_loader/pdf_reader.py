from pypdf import PdfReader


def read_pdf(pdf_path: str) -> str:

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text