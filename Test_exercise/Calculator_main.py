from Calculator import Calculator

class Price_calc:
    def __init__(self):
        self.calc = Calculator()

    def get_vat_value(self):
        return self.calc.get_vat()

    def get_user_new_vat(self, new_user_vat: float):
        self.calc.change_vat(new_user_vat)
        return self.get_vat_value()

    def get_user_brutto_price(self, money: float):
        brutto_price = self.calc.calculate_brutto_price(money)
        return brutto_price

    def user_interface(self):
        print("Hello welcome to my application")
        user_vat_input = float(input("Enter your Vat: "))
        new_user_vat = self.calc.change_vat(user_vat_input)
        user_netto_input = float(input("Enter your netto price : "))
        user_netto_price = self.calc.calculate_brutto_price(user_netto_input)
        print("Your Brutto price will be : {}".format(user_netto_price))








nowy_kalkulator = Price_calc()
nowy_kalkulator.user_interface()

