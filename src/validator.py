
from decimal import Decimal, InvalidOperation


def validate_invoice(invoice: dict) -> dict:
    """Check required fields and invoice arithmetic."""

    required_fields = [
        "supplier_name",
        "invoice_number",
        "invoice_date",
        "currency",
        "subtotal",
        "tax",
        "total",
    ]

    errors = []

    for field in required_fields:
        value = invoice.get(field)

        if value is None or (
            isinstance(value, str) and not value.strip()
        ):
            errors.append(f"Missing required field: {field}")

    if errors:
        return {"valid": False, "errors": errors}

    try:
        subtotal = Decimal(str(invoice["subtotal"]))
        tax = Decimal(str(invoice["tax"]))
        total = Decimal(str(invoice["total"]))

        if not all(
            amount.is_finite()
            for amount in (subtotal, tax, total)
        ):
            raise InvalidOperation

    except (InvalidOperation, ValueError, TypeError):
        return {
            "valid": False,
            "errors": [
                "Subtotal, tax, and total must be valid finite numbers."
            ],
        }

    if subtotal < 0 or tax < 0 or total < 0:
        errors.append("Invoice amounts cannot be negative.")

    if subtotal + tax != total:
        errors.append(
            f"Total mismatch: expected {subtotal + tax}, "
            f"but received {total}."
        )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }
