from Person import Person
from Virus import Virus
import random
random.seed(1)

class Simulater(object):
    def __init__(self, population, virus_name):
        self.population = population
        self.virus_name = virus_name
        self.people = {}
        self.infected_people = {}
        self.vaccinated_people = {}
        self.rest_people = {}
        self.first_infected = 0
        self.vaccination_rate = 0
        self.dead = 0

    def create_people(self):
        i = 0
        while i < self.population:
            self.people[i] = Person()
            i += 1

    def decide_rate(self):
        self.first_infected = round(random.random(), 2)
        self.vaccination_rate = round(random.random(), 2)
        print("%s %s" % (self.first_infected, self.vaccination_rate))

    def people_get_infectd_or_vaccinated(self):
        self.create_people()
        self.decide_rate()
        number_of_infected_people = self.population * self.first_infected
        i = 0
        while i < int(number_of_infected_people):
            self.people[i].sick = True
            self.infected_people[i] = self.people[i]
            i += 1
        number_of_vaccinated_people = (self.population - number_of_infected_people) * self.vaccination_rate
        while i < int(number_of_infected_people) + int(number_of_vaccinated_people):
            self.people[i].vaccinated = True
            self.vaccinated_people[i] = self.people[i]
            i += 1
        while i < self.population:
            self.rest_people[i] = self.people[i]
            i += 1
        print("%s %s %s %s" % (int(number_of_infected_people), int(number_of_vaccinated_people),  self.dead, len(self.rest_people)))

    def people_die_or_infect(self):
        self.people_get_infectd_or_vaccinated()
        virus = Virus(self.virus_name)
        virus.set_detail()
        for person in self.people:
            if self.people[person].sick is True:
                number = random.randint(1, 100)
                if number <= virus.deadliness * 100:
                    self.people[person].death = True
                    self.infected_people.pop(person)
                    self.dead += 1
                else:
                    i = 0
                    while i < int(virus.contagiousness):
                        pick_number = random.randint(0, (self.population - 1))
                        if self.people[pick_number].sick is False and self.people[pick_number].vaccinated is False:
                            self.people[pick_number].sick = True
                            self.infected_people[pick_number] = self.people[pick_number]
                            self.rest_people.pop(pick_number)
                        else:
                            pass
                        i += 1
            else:
                pass
        print("%s %s %s %s" % (len(self.infected_people), len(self.vaccinated_people), self.dead, len(self.rest_people)))


simu = Simulater(10, "Melaria")
simu.people_die_or_infect()
