import pytest
from Virus import Virus
from Simulater import Simulater
from Person import Person
import random
random.seed(1)

def set_up_test():
    simu = Simulater(1000, 0.90, "Ebola", 10)
    return simu

def test_init():
    simu = set_up_test()
    assert simu.population == 1000
    assert simu.virus.name == "Ebola"
    assert simu.people == {}
    assert simu.infected_people == 0
    assert simu.vaccinated_people == 0
    assert simu.regular_people == 0
    assert simu.first_infected == 10
    assert simu.vaccination_rate == 0.90
    assert simu.dead == 0

def test_create_people():
    simu = set_up_test()
    simu.create_people()
    assert len(simu.people) == 1000

def test_people_get_infectd_or_vaccinated():
    simu = set_up_test()
    simu.people_get_infectd_or_vaccinated()
    assert simu.infected_people == 10
    assert simu.vaccinated_people == 891
    assert simu.regular_people == 99

def test_people_die_or_overcome():
    simu = set_up_test()
    simu.people_get_infectd_or_vaccinated()
    simu.people_die_or_overcome()
    assert simu.infected_people + simu.vaccinated_people + simu.dead + simu.regular_people == 1000

def test_iterate_simu():
    simu = set_up_test()
    simu.people_get_infectd_or_vaccinated()
    simu.iterate_simu()
    assert simu.infected_people == 0
    assert simu.infected_people + simu.vaccinated_people + simu.dead + simu.regular_people == 1000
