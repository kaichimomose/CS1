from student import Student


class Classroom(object):
    """docstring fo Classroom."""
    def __init__(self, class_name):
        self.class_name = class_name
        self.day_time = {}
        self.students = {}
        self.students_name = []
        self.assignments = []
        self.students_grades = {}
        print("you create the %s class" % self.class_name)

    def command(self):
        print("The command list")
        print("as: add a student, rs: remove a student,")
        print("aa: add an assignment, ra: remove an assignment,")
        print("ac: add a day to the class schedule, rc: remove a day from the class schedule,")
        print("c: calculate average of each student's grades,")
        print("s: see class detail, e: exit the %s class: " % self.class_name)
        command = input("Type a command: ")
        if command == "as":
            self.add_student()
        elif command == "rs":
            self.remove_student()
        elif command == "aa":
            self.add_assignment()
        elif command == "ra":
            self.remove_assignment()
        elif command == "ac":
            self.add_class_schedule()
        elif command == "rc":
            self.remove_class_schedule()
        elif command == "c":
            self.calculate_average_grade()
        elif command == "s":
            self.see_class_detail()
        elif command == "e":
            return
        else:
            pass
        self.command()

    def add_class_schedule(self):
        day = input("When is the %s class: " % self.class_name)
        self.day_time[day] = input("What time does it start on %s: " % day)
        more_day = input("Do you add other days? (yes or no): ")
        print(self.day_time)
        if more_day == "yes":
            self.add_class_schedule()
        else:
            return

    def remove_class_schedule(self):
        day = input("What date do you want to remove? The class schedule is now %s: " % self.day_time)
        for a_day_time in self.day_time:
            if day == a_day_time:
                self.day_time.pop(day)
                print("%s has been removed from the %s class" % (day, self.class_name))
                print("Now the %s schedule is %s" % self.day_time)
            else:
                pass

    def calculate_average_grade(self):
        for student in self.students:
            if self.students[student].assignment_grade == {}:
                self.students_grades[student] = 0.0
            else:
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
        self.students_name.append(name)
        print("%s has %s" % (self.class_name, self.students_name))

    def remove_student(self):
        name = input("Who will you remove from the %s class: " % self.class_name)
        for student_name in self.students_name:
            if name == student_name:
                self.students.pop(name)
                self.students_name.remove(name)
                print("%s has been removed from the %s class" % (name, self.class_name))
                print("Now %s has %s" % (self.class_name, self.students_name))
            else:
                pass

    def add_assignment(self):
        assignment = input("What is the assignment name: ")
        print("you give students %s for assignment" % assignment)
        for student in self.students:
            grade = input("%s's %s grade: " % (student, assignment))
            if grade.isdigit() is True:
                self.students[student].assignment_grade[assignment] = int(grade)
            else:
                print("Type digit! Try again.")
                return
        if assignment not in self.assignments:
            self.assignments.append(assignment)

    def remove_assignment(self):
        all_or_one = input("Do you want to remove an assignment from all students' lists or just one student's list? (type all or one): ")
        if all_or_one == "all":
            assignment = input("Which assignment do you remove? %s: " % (self.assignments))
            self.assignments.remove(assignment)
            for student_name in self.students_name:
                for assignment_name in self.students[student_name].assignment_grade:
                    if assignment == assignment_name:
                        self.students[student_name].assignment_grade.pop(assignment)
                        print("%s has been removed from %s's assignment lists" % (assignment, student_name))
                        return
                    else:
                        pass
        elif all_or_one == "one":
            name = input("Whose assignment do you remove: ")
            for student_name in self.students_name:
                if name == student_name:
                    assignment = input("Which assignment do you remove? %s has %s: " % (name, self.students[name].assignment_grade))
                    for assignment_name in self.students[name].assignment_grade:
                        if assignment == assignment_name:
                            self.students[name].assignment_grade.pop(assignment)
                            print("%s has been removed from %s's assignment lists" % (assignment, name))
                            return
                        else:
                            pass
        else:
            pass

    def see_class_detail(self):
        print("This class is " + self.class_name)
        print(self.day_time)
        print(self.assignments)
        print(self.students_grades)
        for name in self.students_name:
            print("%s %s" % (name, self.students[name].assignment_grade))
