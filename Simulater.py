from Person import Person
from Virus import Virus
from logger import Logger
import random
random.seed(1)

class Simulater(object):
    def __init__(self, population, virus_name):
        self.population = population
        self.virus = Virus(virus_name)
        self.people = {}
        self.infected_people = {}
        self.vaccinated_people = {}
        self.regular_people = {}
        self.first_infected = round(random.random(), 2)
        self.vaccination_rate = round(random.random(), 2)
        self.dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population, self.vaccination_rate, self.first_infected)
        self.logger = Logger(self.file_name)

    def create_people(self):
        i = 0
        while i < self.population:
            self.people[i] = Person()
            i += 1

    def people_get_infectd_or_vaccinated(self):
        self.virus.set_detail()
        self.create_people()
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
            self.regular_people[i] = self.people[i]
            i += 1
        print("number_of_infected_people, number_of_vaccinated_people, dead, rest_people")
        print("%s %s %s %s" % (int(number_of_infected_people), int(number_of_vaccinated_people), self.dead, len(self.regular_people)))
        self.logger.write_metadata(self.population, self.vaccination_rate, self.virus.name, self.virus.deadliness, self.virus.contagiousness)

    def people_die_or_overcome(self):
        for person in self.people:
            if self.people[person].death is False and self.people[person].sick is True:
                i = 0
                while i < int(self.virus.contagiousness):
                    pick_number = random.randint(0, (self.population - 1))
                    if self.people[pick_number].sick is False and self.people[pick_number].vaccinated is False:
                        did_infect = True
                        self.people[pick_number].sick = True
                        self.infected_people[pick_number] = self.people[pick_number]
                        self.regular_people.pop(pick_number)
                    else:
                        did_infect = False
                    self.logger.log_interaction(person, pick_number, did_infect, self.people[pick_number].vaccinated, self.people[pick_number].sick)
                    i += 1
                number = random.randint(1, 100)
                if number <= self.virus.deadliness * 100:
                    self.people[person].death = True
                    self.dead += 1
                else:
                    self.people[person].sick = False
                    self.people[person].vaccinated = True
                    self.vaccinated_people[person] = self.people[person]
                self.logger.log_infection_survival(person, self.people[person].death)
                self.infected_people.pop(person)
            else:
                pass
        print("%s %s %s %s" % (len(self.infected_people), len(self.vaccinated_people), self.dead, len(self.regular_people)))

    def iterate_simu(self):
        self.people_get_infectd_or_vaccinated()
        i = 1
        while len(self.infected_people) > 0:
            self.people_die_or_overcome()
            self.logger.log_time_step(i)
            i += 1


simu = Simulater(30000, "Cholera")
simu.iterate_simu()
