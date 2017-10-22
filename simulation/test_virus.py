import pytest
from Virus import Virus

def set_up_test():
    virus = Virus("Malaria")
    return virus

def test_init():
    virus = set_up_test()
    assert virus.name == "Malaria"
    assert virus.deadliness == 0
    assert virus.contagiousness == 0

def test_set_detail():
    virus = set_up_test()
    virus.set_detail()
    assert virus.deadliness == 0.3
    assert virus.contagiousness == 15
