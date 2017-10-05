class Classroom(object):
    """docstring fo Classroom."""
    def __init__(self, class_name):
        self.class_name = class_name
        self.day_time = {}
        self.students = {}
        self.assignments = []
        self.students_grades = {}
        print("you create the %s class" % self.class_name)

    def command(self):
        command = input("Type a command (as: add a student, rs: remove a student, aa: add an assignment, ra: remove an assignment, c: calculate average of each student's grades, s: see class detail, e: exit the %s class): " % self.class_name)
        if command == "as":
            self.add_student()
        elif command == "rs":
            self.remove_student()
        elif command == "aa":
            self.add_assignment()
        elif command == "ra":
            self.remove_assignment()
        elif command == "c":
            self.calculate_average_grade()
        elif command == "s":
            self.see_class_detail()
        elif command == "e":
            make_school.creat_classes()
        else:
            pass
        self.command()

    def class_schedule(self):
        day = input("When is the %s class: " % self.class_name)
        self.day_time[day] = input("What time does it start on %s: " % day)
        more_day = input("Do you add other days? (yes or no): ")
        print(self.day_time)
        if more_day == "yes":
            self.class_schedule()
        else:
            return

    def calculate_average_grade(self):
        for student in self.students:
            total_grade = self.students[student].total_grade
            for item in self.students[student].assignment_grade:
                total_grade += self.students[student].assignment_grade[item]
            average = total_grade/len(self.students[student].assignment_grade)
            self.students_grades[student] = round(average, 2)
        print(self.students_grades)

    def add_student(self):
        name = input("Who will you add to the %s class: " % self.class_name)
        on_time = input("He/She join in the %s class on time or late?: " % self.class_name)
        self.students[name] = Student(name, on_time)
        print("%s has been added to the %s class" % (name, self.class_name))
        if on_time == "late":
            print("%s joined in the %s class late" % (name, self.class_name))
        student_name = []
        for student in self.students:
            student_name.append(student)
        print("%s has %s" % (self.class_name, student_name))

    def remove_student(self):
        name = input("Who will you remove from the %s class: " % self.class_name)
        self.students.pop(name)
        print("%s has been removed from the %s class" % (name, self.class_name))
        student_name = []
        for student in self.students:
            student_name.append(student)
        print("Now %s has %s" % (self.class_name, student_name))

    def add_assignment(self):
        assignment = input("What is the assignment name: ")
        if assignment not in self.assignments:
            self.assignments.append(assignment)
        print("you give students %s for assignment" % assignment)
        for student in self.students:
            self.students[student].assignment_grade[assignment] = int(input("%s's %s grade: " % (student, assignment)))

    def remove_assignment(self):
        name = input("Whose assignment do you remove: ")
        assignment = input("Which assignment do you remove? %s has %s: " % (name, self.students[name].assignment_grade))
        self.students[name].assignment_grade.pop(assignment)

    def see_class_detail(self):
        print(self.class_name)
        print(self.day_time)
        print(self.assignments)
        print(self.students_grades)


class Student(object):
    def __init__(self, name, on_time):
        self.name = name
        self.on_time = on_time
        self.assignment_grade = {}
        self.total_grade = 0
        self.number_assignment = 0
        self.excused_absent = 0


class School(object):
    def __init__(self):
        self.class_rooms = {}
        self.class_roster = []

    def creat_classes(self):
        print(self.class_rooms)
        print(self.class_roster)
        if self.class_rooms == {}:
            creat_class = input("Do you want to create a class? (yes or no): ")
        else:
            creat_class = input("Do you want to create other class? (yes or no): ")
        if creat_class == "yes":
            class_name = input("What is name of the class: ")
            self.class_roster.append(class_name)
            self.class_rooms[class_name] = Classroom(class_name)
            print(self.class_rooms)
            self.class_rooms[class_name].class_schedule()
            self.class_rooms[class_name].command()
        else:
            if self.class_roster != []:
                class_name = input("Do you want to access to a exist class? Exist classes are %s: " % self.class_roster)
                self.class_rooms[class_name].command()
            else:
                pass
        self.creat_classes()


make_school = School()
make_school.creat_classes()
