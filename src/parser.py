
import re


def parse_invoice_text(text: str) -> dict:
    """Convert extracted invoice text into structured data."""

    patterns = {
        "supplier_name": r"Supplier:\s*(.+)",
        "invoice_number": r"Invoice Number:\s*(.+)",
        "invoice_date": r"Date:\s*(.+)",
        "currency": r"Currency:\s*([A-Z]{3})",
        "subtotal": r"^\s*Subtotal:\s*([\d,]+(?:\.\d{1,2})?)",
        "tax": r"^\s*Tax:\s*([\d,]+(?:\.\d{1,2})?)",
        "total": r"^\s*Total:\s*([\d,]+(?:\.\d{1,2})?)",
    }

    invoice = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)

        if match:
            value = match.group(1).strip()

            if field in ["subtotal", "tax", "total"]:
                value = value.replace(",", "")

            invoice[field] = value
        else:
            invoice[field] = None

    return invoice
