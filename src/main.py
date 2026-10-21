
import json
from pathlib import Path

from src.validator import validate_invoice


def main():
    invoice_path = (
        Path(__file__).resolve().parent.parent
        / "sample_data"
        / "invoice.json"
    )

    with invoice_path.open("r", encoding="utf-8") as file:
        invoice = json.load(file)

    result = validate_invoice(invoice)

    print("\nInvoice Intelligence & Approval Copilot")
    print("-" * 42)
    print(f"Invoice: {invoice.get('invoice_number')}")
    print(f"Supplier: {invoice.get('supplier_name')}")
    print(f"Valid: {result['valid']}")

    if result["errors"]:
        print("Issues found:")
        for error in result["errors"]:
            print(f"- {error}")
    else:
        print("No validation issues found.")


if __name__ == "__main__":
    main()
