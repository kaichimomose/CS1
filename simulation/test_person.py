import pytest
from Person import Person

def set_up_test():
    person = Person()
    return person

def test_init():
    person = set_up_test()
    assert person.vaccinated is False
    assert person.sick is False
    assert person.death is False
