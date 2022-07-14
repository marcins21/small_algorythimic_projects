import pytest

from Calculator import Calculator

class TestCalculator:

    def test_adding_two_numbers(self):
        the_sum = 2+2
        assert the_sum == 4

    def test_calculation_netto_price_with_default_value(self):
        calc = Calculator()
        result = calc.calculate_brutto_price(100)
        assert result == 123

    def test_calculation_netto_price_with_diffrent_value(self):
        calc = Calculator()
        vat = calc.change_vat(0.5)
        result = calc.calculate_brutto_price(100)
        assert result == 150

