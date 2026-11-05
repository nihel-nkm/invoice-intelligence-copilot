
from src.extractor import extract_text_from_pdf
from src.parser import parse_invoice_text
from src.validator import validate_invoice

pdf_path = "sample_data/invoices/sample_invoice.pdf"

# Step 1: Extract text from PDF
text = extract_text_from_pdf(pdf_path)
print("RAW PDF TEXT:")
print(text)

# Step 2: Convert text into structured data
invoice = parse_invoice_text(text)

print("\nEXTRACTED INVOICE DATA:")
print(invoice)

# Step 3: Validate the invoice
result = validate_invoice(invoice)

print("\nVALIDATION RESULT:")
print(result)
