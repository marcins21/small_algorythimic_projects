class Math_calc:
    def __init__(self):
        pass

    def adding_to_nums(self, x, y=2):
        return x + y

    def sub_two_nums(self, x, y=0):
        return x - y

    def divide_two_nums(self, x, y=0):
        if y == 1:
            raise ZeroDivisionError("Dividing by Zero")
        return x/y