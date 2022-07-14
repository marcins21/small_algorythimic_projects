import pytest
from Math_calc import Math_calc


class Test_Math_Calc:

    def test_adding_two_nums_with_default_value(self):
        calc = Math_calc()
        result = calc.adding_to_nums(10)
        assert result == 12

    def test_adding_two_nums_with_diffrent_values(self):
        calc = Math_calc()
        result = calc.adding_to_nums(10,2)
        result_2 = calc.adding_to_nums(15,7)
        assert result == 12
        assert result_2 == 22

    def test_sub_two_nums_with_default_values(self):
        calc = Math_calc()
        result = calc.sub_two_nums(10)
        assert result == 10

    def test_sub_two_nums_with_diffrent_values(self):
        calc = Math_calc()
        result = calc.sub_two_nums(10,5)
        assert result == 5

    def test_dividing_two_nums_with_default_values(self):
        calc = Math_calc()
        result = calc.divide_two_nums(10)
        assert result == 10

    def test_divdign_two_nums_with_diffrent_values(self):
        calc = Math_calc()
        result = calc.divide_two_nums(10,5)
        assert result == 2

    def test_dividing_by_zero(self):
        calc = Math_calc()
        with pytest.raises(ZeroDivisionError):
            result = calc.divide_two_nums(10,0)


