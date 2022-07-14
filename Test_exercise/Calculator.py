class Calculator:
    def __init__(self):
        self.vat = 0.23

    def get_vat(self):
        return self.vat

    def calculate_brutto_price(self, money: int):
        return money*(self.vat+1)

    def change_vat(self, new_vat: float):
        if new_vat <= 0 or new_vat >= 1:
            raise ValueError("Vat must be between 0 and 1")
        self.vat = new_vat



