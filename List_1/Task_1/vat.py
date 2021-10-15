import decimal as dec


class VatCounter():
    """Count VAT using floats"""
    VAT = 0.23

    @classmethod
    def vat_faktura(cls, costs: list[float]) -> float:
        """Counts vat for invoices"""
        return cls.VAT * sum(costs)

    @classmethod
    def vat_paragon(cls, costs: list[float]) -> float:
        """Counts VAT for receipts"""
        return sum([x * cls.VAT for x in costs])


class VatCounterDec():
    """Count VAT using Decimal"""
    VAT = dec.Decimal('0.23')

    @classmethod
    def vat_faktura(cls, costs: list[dec.Decimal]) -> dec.Decimal:
        """Counts vat for invoices"""
        return cls.VAT * sum(costs)

    @classmethod
    def vat_paragon(cls, costs: list[dec.Decimal]) -> dec.Decimal:
        """Counts VAT for receipts"""
        return sum([x * cls.VAT for x in costs])
