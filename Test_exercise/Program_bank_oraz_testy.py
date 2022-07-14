import pytest
class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self,money: int):
        if self.amount >= money:
            self.amount -= money
        else:
            raise NotEnoughtMoney()

    #Getter current amount of money
    def get_current_money_amount(self):
        return self.amount

#Exception of not enought money in the bank
class NotEnoughtMoney(Exception):
    pass


#TESTS

class TestBank:
    def test_creating_bank(self):
        #given
        bank = Bank()

        #when
        starting_amount_of_money = bank.get_current_money_amount()

        #then
        assert starting_amount_of_money == 0
        assert isinstance(bank, Bank) == True

    def test_adding_money(self):
        #given
        bank = Bank()

        #when
        bank.add_money(100)
        money_in_the_bank = bank.get_current_money_amount()

        #Checking if more added money will sum
        bank.add_money(100)
        money_in_the_bank_after_adding = bank.get_current_money_amount()

        #then
        assert money_in_the_bank == 100
        assert  money_in_the_bank_after_adding == 200

    def test_withdrawing_money(self):
        #given
        bank = Bank()
        bank.add_money(100)

        #when
        bank.withdraw_money(50)
        withdrawing_money = bank.get_current_money_amount()

        bank.withdraw_money(50)
        withdrawing_money_more = bank.get_current_money_amount()


        #then
        assert withdrawing_money == 50
        assert withdrawing_money_more == 0



    def test_not_enought_money_cornerCase(self):
        with pytest.raises(NotEnoughtMoney):
            # given
            bank = Bank()

            # when
            not_enoght_money = bank.withdraw_money(100)




