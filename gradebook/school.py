from classroom import Classroom

class School(object):
    def __init__(self):
        self.class_rooms = {}
        self.class_roster = []

    def creat_classes(self):
        if self.class_rooms == {}:
            creat_class = input("Do you want to create a class? (yes or no): ")
        else:
            creat_class = input("Do you want to create another class? (yes or no): ")
        if creat_class == "yes":
            class_name = input("What is name of the class: ")
            self.class_roster.append(class_name)
            self.class_rooms[class_name] = Classroom(class_name)
            print(self.class_rooms)
            self.class_rooms[class_name].add_class_schedule()
            self.class_rooms[class_name].command()
        else:
            if self.class_rooms != {}:
                class_name = input("Do you want to access to a existing class? Existing classes are %s: " % self.class_roster)
                self.class_rooms[class_name].command()
            else:
                pass
        self.creat_classes()


make_school = School()
make_school.creat_classes()
