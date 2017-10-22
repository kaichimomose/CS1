class Virus(object):
    def __init__(self, name):
        self.name = name
        self.deadliness = 0
        self.contagiousness = 0

    def set_detail(self):
        if self.name == "Cholera":
            self.deadliness = 0.1
            self.contagiousness = 2

        elif self.name == "Ebola":
            self.deadliness = 0.7
            self.contagiousness = 2.3

        elif self.name == "Malaria":
            self.deadliness = 0.3
            self.contagiousness = 15
