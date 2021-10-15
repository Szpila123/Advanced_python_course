import decimal as dec

class VatCounter():
    VAT = 0.23
    @classmethod
    def vat_faktura(cls, costs: list[float]) -> float:
        return cls.VAT * sum(costs)

    @classmethod
    def vat_paragon(cls, costs: list[float]) -> float:
        return sum([x * cls.VAT for x in costs])

class VatCounterDec():
    VAT = dec.Decimal('0.23')
    @classmethod
    def vat_faktura(cls, costs: list[dec.Decimal]) -> dec.Decimal:
        return cls.VAT * sum(costs)

    @classmethod
    def vat_paragon(cls, costs: list[dec.Decimal]) -> dec.Decimal:
        return sum([x * cls.VAT for x in costs])
