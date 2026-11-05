
from src.parser import parse_invoice_text


def test_parser_extracts_all_invoice_fields():
    text = """
    INVOICE
    Supplier: ABC Technologies
    Invoice Number: INV-101
    Date: 05-11-2026
    Currency: INR
    Subtotal: 10000
    Tax: 1800
    Total: 11800
    """

    invoice = parse_invoice_text(text)

    assert invoice["supplier_name"] == "ABC Technologies"
    assert invoice["invoice_number"] == "INV-101"
    assert invoice["invoice_date"] == "05-11-2026"
    assert invoice["currency"] == "INR"
    assert invoice["subtotal"] == "10000"
    assert invoice["tax"] == "1800"
    assert invoice["total"] == "11800"


def test_parser_does_not_confuse_subtotal_with_total():
    text = """
    Subtotal: 10000
    Tax: 1800
    Total: 11800
    """

    invoice = parse_invoice_text(text)

    assert invoice["subtotal"] == "10000"
    assert invoice["total"] == "11800"


def test_parser_handles_missing_tax():
    text = """
    Supplier: ABC Technologies
    Invoice Number: INV-101
    Date: 05-11-2026
    Currency: INR
    Subtotal: 10000
    Total: 10000
    """

    invoice = parse_invoice_text(text)

    assert invoice["tax"] is None
