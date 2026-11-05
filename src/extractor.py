
import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a text-based PDF invoice."""

    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

    return extracted_text
