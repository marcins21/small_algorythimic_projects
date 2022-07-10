import pytest


def sort_by(first_letter=False,last_letter=False, lenght=False):
    names = ["Ala","Barcin","Comasz","Darek","Elina"]
    if first_letter:
        names.sort()
    if last_letter:
        names.sort(key=lambda name: name[::-1])
    if lenght:
        names.sort(key=len)
    return names

class TestSort:
    @pytest.fixture
    def names(self):
        return ["Ala","Barcin","Comasz","Darek","Elina"]

    def test_sort_first_letter(self,names):
        #when
        sorted_names = sort_by(first_letter=True)

        #then
        assert sorted_names == ['Ala', 'Barcin', 'Comasz', 'Darek', 'Elina']

    def test_sort_last_letter(self,names):
        #when
        sorted_names = sort_by(last_letter=True)

        #then
        assert sorted_names == ['Ala', 'Elina', 'Darek', 'Barcin', 'Comasz']

    def test_sort_lenght(self,names):
        #when
        sorted_names = sort_by(lenght=True)

        #then
        assert sorted_names == ['Ala', 'Darek', 'Elina', 'Barcin', 'Comasz']