from decimal import Context, Decimal, Inexact

# Strict context: raises Inexact if rounding would lose digits.
_STRICT = Context(traps=[Inexact])


def to_cents(amount: str) -> int:
    """Convert a refund amount string like '10.50' to integer cents."""
    value = Decimal(amount).quantize(Decimal("0.01"), context=_STRICT)
    return int(value * 100)


def process_refund(order_total_cents: int, amount: str) -> dict:
    cents = to_cents(amount)
    if cents <= 0:
        raise ValueError("refund must be positive")
    if cents > order_total_cents:
        raise ValueError("refund exceeds order total")
    return {"status": "refunded", "cents": cents}
