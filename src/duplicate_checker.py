
def find_duplicate_invoice(
    new_invoice: dict,
    existing_invoices: list[dict],
) -> dict:
    """Check whether an invoice number already exists for a supplier."""

    supplier = new_invoice.get("supplier_name", "").strip().casefold()
    invoice_number = (
        new_invoice.get("invoice_number", "").strip().casefold()
    )

    if not supplier or not invoice_number:
        return {
            "is_duplicate": False,
            "reason": "Supplier name and invoice number are required.",
        }

    for existing in existing_invoices:
        existing_supplier = (
            existing.get("supplier_name", "").strip().casefold()
        )
        existing_number = (
            existing.get("invoice_number", "").strip().casefold()
        )

        if (
            supplier == existing_supplier
            and invoice_number == existing_number
        ):
            return {
                "is_duplicate": True,
                "reason": (
                    f"Invoice {new_invoice['invoice_number']} "
                    f"from {new_invoice['supplier_name']} "
                    "already exists."
                ),
            }

    return {
        "is_duplicate": False,
        "reason": "No duplicate invoice found.",
    }
