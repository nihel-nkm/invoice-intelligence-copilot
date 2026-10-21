
from src.validator import validate_invoice


def valid_invoice():
    return {
        "supplier_name": "Malabar Office Supplies",
        "invoice_number": "MOS-2026-001",
        "invoice_date": "2026-10-15",
        "currency": "INR",
        "subtotal": 10000.00,
        "tax": 1800.00,
        "total": 11800.00,
    }


def test_valid_invoice_passes():
    result = validate_invoice(valid_invoice())
    assert result["valid"] is True
    assert result["errors"] == []


def test_incorrect_total_fails():
    invoice = valid_invoice()
    invoice["total"] = 12000.00

    result = validate_invoice(invoice)

    assert result["valid"] is False
    assert any("Total mismatch" in e for e in result["errors"])


def test_missing_supplier_fails():
    invoice = valid_invoice()
    invoice["supplier_name"] = ""

    result = validate_invoice(invoice)

    assert result["valid"] is False
    assert any("supplier_name" in e for e in result["errors"])


def test_negative_amount_fails():
    invoice = valid_invoice()
    invoice["subtotal"] = -100.00

    result = validate_invoice(invoice)

    assert result["valid"] is False
    assert any("negative" in e for e in result["errors"])
