from Person import Person
from Virus import Virus
from logger import Logger
import random, sys
random.seed(1)

class Simulater(object):
    def __init__(self, population, vaccination_rate, virus_name, first_infected):
        if population < 1000:
            self.population = 1000
        else:
            self.population = population
        self.virus = Virus(virus_name)
        self.people = {}
        self.infected_people = 0
        self.vaccinated_people = 0
        self.regular_people = 0
        self.first_infected = first_infected
        self.vaccination_rate = vaccination_rate
        self.dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}".format(
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
        number_of_infected_people = self.first_infected
        i = 0
        number_of_vaccinated_people = (self.population - self.first_infected) * self.vaccination_rate
        while i < int(number_of_vaccinated_people):
            self.people[i].vaccinated = True
            self.vaccinated_people += 1
            i += 1
        while i < int(number_of_infected_people) + int(number_of_vaccinated_people):
            self.people[i].sick = True
            self.infected_people += 1
            i += 1
        while i < self.population:
            self.regular_people += 1
            i += 1
        print("number_of_infected_people, number_of_vaccinated_people, dead, regular_people")
        print("%s %s %s %s" % (int(number_of_infected_people), int(number_of_vaccinated_people), self.dead, self.regular_people))
        self.logger.write_metadata(self.population, self.first_infected, self.vaccination_rate, self.virus.name, self.virus.deadliness, self.virus.contagiousness)

# number_of_infected_people = self.population * self.first_infected
# i = 0
# while i < int(number_of_infected_people):
#     self.people[i].sick = True
#     self.infected_people[i] = self.people[i]
#     i += 1
# number_of_vaccinated_people = (self.population - number_of_infected_people) * self.vaccination_rate
# while i < int(number_of_infected_people) + int(number_of_vaccinated_people):
#     self.people[i].vaccinated = True
#     self.vaccinated_people[i] = self.people[i]
#     i += 1
# while i < self.population:
#     self.regular_people[i] = self.people[i]
#     i += 1

    def people_die_or_overcome(self):
        infected_people_list = []
        for person in self.people:
            if self.people[person].death is False and self.people[person].sick is True and person not in infected_people_list:
                number = random.random()
                percentage = self.virus.contagiousness - int(self.virus.contagiousness)
                if number <= percentage:
                    contagiousness = int(self.virus.contagiousness)
                else:
                    contagiousness = int(self.virus.contagiousness) + 1
                i = 0
                j = 0
                hundred_people_list = []
                while i < contagiousness and j < 100:
                    pick_person = random.randint(0, (self.population - 1))
                    if pick_person != person and pick_person not in hundred_people_list and self.people[pick_person].death is False:
                        hundred_people_list.append(pick_person)
                        j += 1
                        if self.people[pick_person].sick is False and self.people[pick_person].vaccinated is False:
                            did_infect = True
                            self.people[pick_person].sick = True
                            self.infected_people += 1
                            self.regular_people -= 1
                            infected_people_list.append(pick_person)
                            i += 1
                        else:
                            did_infect = False
                            i += 0
                        self.logger.log_interaction(person, pick_person, did_infect, self.people[pick_person].vaccinated, self.people[pick_person].sick)
                    else:
                        pass
                number = random.randint(1, 100)
                if number <= self.virus.deadliness * 100:
                    self.people[person].death = True
                    self.dead += 1
                else:
                    self.people[person].sick = False
                    self.people[person].vaccinated = True
                    self.vaccinated_people += 1
                self.logger.log_infection_survival(person, self.people[person].death)
                self.infected_people -= 1
            else:
                pass
        print("%s %s %s %s" % (self.infected_people, self.vaccinated_people, self.dead, self.regular_people))

    # i = 0
    # number = random.random()
    # percentage = self.virus.contagiousness - int(self.virus.contagiousness)
    # if number <= percentage:
    #     contagiousness = int(self.virus.contagiousness)
    # else:
    #     contagiousness = int(self.virus.contagiousness) + 1
    # while i < contagiousness:
    #     pick_number = random.randint(0, (self.population - 1))
    #     if self.people[pick_number].death is True:
    #         i += 0
    #     else:
    #         if self.people[pick_number].sick is False and self.people[pick_number].vaccinated is False:
    #             did_infect = True
    #             self.people[pick_number].sick = True
    #             self.infected_people[pick_number] = self.people[pick_number]
    #             self.regular_people.pop(pick_number)
    #         else:
    #             did_infect = False
    #         self.logger.log_interaction(person, pick_number, did_infect, self.people[pick_number].vaccinated, self.people[pick_number].sick)
    #         i += 1

    def iterate_simu(self):
        self.people_get_infectd_or_vaccinated()
        i = 1
        while self.infected_people > 0:
            self.people_die_or_overcome()
            self.logger.log_time_step(i, self.infected_people, self.vaccinated_people, self.dead, self.regular_people)
            i += 1


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    if len(params) == 4:
        initial_infected = int(params[3])
    else:
        initial_infected = 1
    simu = Simulater(pop_size, vacc_percentage, virus_name, initial_infected)
    simu.iterate_simu()
