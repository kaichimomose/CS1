from classroom_for_test import Classroom

class School(object):
    def __init__(self):
        self.class_rooms = {}
        self.class_roster = []

    def creat_classes(self, creat_class, class_name):
        if self.class_rooms == {}:
            creat_class = creat_class
        else:
            creat_class = creat_class
        if creat_class == "yes":
            class_name = class_name
            self.class_roster.append(class_name)
            self.class_rooms[class_name] = Classroom(class_name)
            print(self.class_rooms)
            self.class_rooms[class_name].add_class_schedule('Monday', '10:00', 'no')
            self.class_rooms[class_name].command('as')
        else:
            if self.class_rooms != {}:
                class_name = class_name
                self.class_rooms[class_name].command('rc')
            else:
                pass
