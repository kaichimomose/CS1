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

    def command(self, command):
        print("The command list")
        print("as: add a student, rs: remove a student,")
        print("aa: add an assignment, ra: remove an assignment,")
        print("ac: add a day to the class schedule, rc: remove a day from the class schedule,")
        print("c: calculate average of each student's grades,")
        print("s: see class detail, e: exit the %s class: " % self.class_name)
        command = command
        if command == "as":
            self.add_student("Chris", "late")
        elif command == "rs":
            self.remove_student("Hadou")
        elif command == "aa":
            self.add_assignment("Fizzbuzz", "50")
        elif command == "ra":
            self.remove_assignment("one", "Fizzbuzz", "Chris")
        elif command == "ac":
            self.add_class_schedule("Thursday", "16:00", "no")
        elif command == "rc":
            self.remove_class_schedule("Monday")
        elif command == "c":
            self.calculate_average_grade()
        elif command == "s":
            self.see_class_detail()
        elif command == "e":
            return 0
        else:
            pass


    def add_class_schedule(self, day, time, more_day):
        day = day
        self.day_time[day] = time
        more_day = more_day
        print(self.day_time)
        if more_day == "yes":
            print("yes")
        else:
            return 0

    def remove_class_schedule(self, day):
        day = day
        if day in self.day_time:
            self.day_time.pop(day)
            print("%s has been removed from the %s class" % (day, self.class_name))
            print("Now the schedule of the %s class is %s" % (self.class_name, self.day_time))
        else:
            return 0

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

    def add_student(self, name, on_time):
        name = name
        on_time = on_time
        self.students[name] = Student(name, on_time)
        print("%s has been added to the %s class" % (name, self.class_name))
        if on_time == "late":
            print("%s joined in the %s class late" % (name, self.class_name))
        self.students_name.append(name)
        print("%s has %s" % (self.class_name, self.students_name))

    def remove_student(self, name):
        name = name
        if name in self.students_name:
            self.students.pop(name)
            self.students_name.remove(name)
            print("%s has been removed from the %s class" % (name, self.class_name))
            print("Now %s has %s" % (self.class_name, self.students_name))
        else:
            return 0

    def add_assignment(self, assignment, grade):
        assignment = assignment
        print("you give students %s for assignment" % assignment)
        for student in self.students:
            grade = grade
            if grade.isdigit() is True:
                self.students[student].assignment_grade[assignment] = int(grade)
            else:
                print("Type digit! Try again.")
                return 0
        if assignment not in self.assignments:
            self.assignments.append(assignment)

    def remove_assignment(self, all_or_one, assignment, name=""):
        all_or_one = all_or_one
        if all_or_one == "all":
            assignment = assignment
            self.assignments.remove(assignment)
            for student_name in self.students_name:
                if assignment in self.students[student_name].assignment_grade:
                    self.students[student_name].assignment_grade.pop(assignment)
                    print("%s has been removed from %s's assignment lists" % (assignment, student_name))
                else:
                    pass
        elif all_or_one == "one":
            name = name
            if name in self.students_name:
                if assignment in self.students[name].assignment_grade:
                    self.students[name].assignment_grade.pop(assignment)
                    print("%s has been removed from %s's assignment lists" % (assignment, name))
                else:
                    pass
        else:
            return 0

    def see_class_detail(self):
        print("This class is " + self.class_name)
        print(self.day_time)
        print(self.assignments)
        print(self.students_grades)
        for name in self.students_name:
            print("%s: %s" % (name, self.students[name].assignment_grade))
