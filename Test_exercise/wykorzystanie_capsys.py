import pytest
class User:
    def __init__(self,name,lastname):
        self.isCreated = True
        self.name = name
        self.lastname = lastname


    def get_user_name(self):
        print(self.name)

    def get_user_lastname(self):
        print(self.lastname)


class TestUser:
    def test_creating_user(self):
        #given
        user = User("Marcin","Sitko")

        #when
        value = user.isCreated

        #then
        assert  value == True
        assert  isinstance(user, User)

    def test_getting_user_name(self,capsys):
        #given
        user = User("Marcin","Sitko")

        #when
        user.get_user_name()
        out,err = capsys.readouterr()

        assert out == "Marcin\n"

    def test_getting_user_lastname(self,capsys):
        #given
        user = User("Tomasz","kowalski")

        #when
        user.get_user_lastname()
        out,err = capsys.readouterr()

        #then
        assert out == "kowalski\n"




