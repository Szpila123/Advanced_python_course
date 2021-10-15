import vat as vat
import decimal as dec

zakupy = ['0.2', '0.5', '4.59', '6']

if __name__ == "__main__":
    zakupy_int = [float(x) for x in zakupy]
    print(vat.VatCounter.vat_faktura(zakupy_int) == vat.VatCounter.vat_paragon(zakupy_int))

    zakupy_dec = [dec.Decimal(x) for x in zakupy]
    print(vat.VatCounterDec.vat_faktura(zakupy_dec) == vat.VatCounterDec.vat_paragon(zakupy_dec))