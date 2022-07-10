import pytest
from zadanie3 import NumberOperations


class Test_NumberOperations:

    def test_number_multiply_default_values(self):
        #given
        number=NumberOperations(10)

        #when
        value = number.number_muliply(2)

        #then
        assert value == 20

    def test_number_multiply_corner_case(self):
        #given
        number = NumberOperations(0)

        #when
        value = number.number_muliply(10)

        #then
        assert value == 0

    def test_number_division_default_values(self):
        #given
        number = NumberOperations(10)
        number1 = NumberOperations(5)

        #when
        value1 = number.number_division(5)
        value2 = number1.number_division(2)

        #then
        assert value1 == 2
        assert value2 == 2.5

    def test_number_division_corner_case(self):
        #given
        number1 = NumberOperations(0)
        number3 = NumberOperations(15)

        #when
        value1 = number1.number_division(5)
        value3 = number3.number_division(1)

        #then
        assert value1 == 0
        assert value3 == 15
        with pytest.raises(ZeroDivisionError):
            number2 = NumberOperations(10)
            value2 = number2.number_division(0)

    def test_number_add(self):
        #given
        number = NumberOperations(10)

        #when
        value = number.number_add(10)

        #then
        assert value == 20

    def test_number_subtruction(self):
        #given
        number = NumberOperations(10)

        #when
        value = number.number_subtruction(10)

        #then
        assert value == 0

    def test_number_power_struck_default_values(self):
        #given
        number = NumberOperations(10)

        #when
        value = number.number_power_struct(2)

        #then
        assert value == 100

    def test_number_power_struct_corner_case(self):
        #given
        number1 = NumberOperations(0)
        number2 = NumberOperations(1)

        #when
        value1 = number1.number_power_struct(10)
        value2 = number1.number_power_struct(0)
        value3 = number2.number_power_struct(0)
        value4 = number2.number_power_struct(10)

        #then
        assert value1 == 0
        assert value2 == 1
        assert value3 == 1
        assert value4 == 1



    def test_number_power_rek_default_values(self):
        # given
        number = NumberOperations(10)
        number2 = NumberOperations(2)

        # when
        value = number.number_power_rek(2)
        value2 = number2.number_power_rek(4)

        # then
        assert value == 100
        assert value2 == 16


    def test_number_power_rek_corner_case(self):
        # given
        number1 = NumberOperations(0)
        number2 = NumberOperations(1)

        # when
        value1 = number1.number_power_struct(10)
        value2 = number1.number_power_struct(0)
        value3 = number2.number_power_struct(0)
        value4 = number2.number_power_struct(10)

        # then
        assert value1 == 0
        assert value2 == 1
        assert value3 == 1
        assert value4 == 1


