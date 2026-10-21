
from src.duplicate_checker import find_duplicate_invoice


def test_duplicate_invoice_is_detected():
    existing = [
        {
            "supplier_name": "Malabar Office Supplies",
            "invoice_number": "MOS-2026-001",
            "total": 11800.00,
        }
    ]

    new_invoice = {
        "supplier_name": "Malabar Office Supplies",
        "invoice_number": "MOS-2026-001",
        "total": 11800.00,
    }

    result = find_duplicate_invoice(new_invoice, existing)

    assert result["is_duplicate"] is True


def test_different_invoice_is_not_duplicate():
    existing = [
        {
            "supplier_name": "Malabar Office Supplies",
            "invoice_number": "MOS-2026-001",
        }
    ]

    new_invoice = {
        "supplier_name": "Malabar Office Supplies",
        "invoice_number": "MOS-2026-002",
    }

    result = find_duplicate_invoice(new_invoice, existing)

    assert result["is_duplicate"] is False


def test_duplicate_check_ignores_case_and_spaces():
    existing = [
        {
            "supplier_name": "Malabar Office Supplies",
            "invoice_number": "MOS-2026-001",
        }
    ]

    new_invoice = {
        "supplier_name": "  MALABAR OFFICE SUPPLIES ",
        "invoice_number": " mos-2026-001 ",
    }

    result = find_duplicate_invoice(new_invoice, existing)

    assert result["is_duplicate"] is True
