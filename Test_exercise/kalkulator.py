
class NumberOperations:

    def __init__(self, number: int):
        self.number = number

    def number_muliply(self, multiplying_number: int) -> int:
        return self.number * multiplying_number

    def number_division(self, division_number: int) -> float:
        if division_number != 0:
            return self.number/division_number
        else:
            raise ZeroDivisionError

    def number_add(self, adding_number: int) -> int:
        return self.number + adding_number

    def number_subtruction(self, subtruct_number: int) -> int:
        return self.number - subtruct_number

    def number_power_struct(self, power_number):
        temp = 1
        for i in range(power_number):
            temp *= self.number
        return temp

    def number_power_rek(self,power_number):
        if power_number == 0:
            return 1
        return self.number * self.number_power_rek(power_number-1)










