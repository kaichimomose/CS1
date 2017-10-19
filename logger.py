class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        f = open('%s.txt' % self.file_name, 'w')
        # print('opened file 1:', self.file_name)
        f.write("%s population %s times people got vaccinated. %s's mortality rate and basic reproduction number are %s and %s\n" % (pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
        f.close()

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        # log every interaction a sick individual has during each time step.
        with open('%s.txt' % self.file_name, 'a') as f:
            # print('opened file 2:', self.file_name)
            f.write("%s %s %s %s %s\n" % (person1, person2, did_infect, person2_vacc, person2_sick))
            # f.close()  # Unneccessary inside "with" block because it's closed automatically

    def log_infection_survival(self, person, did_die_from_infection):
        # log the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("%s %s\n" % (person, did_die_from_infection))

    def log_time_step(self, time_step_number):
        # log when a time step ends, and a new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        with open('%s.txt' % self.file_name, 'a') as f:
            f.write("step %s is done\n" % time_step_number)
