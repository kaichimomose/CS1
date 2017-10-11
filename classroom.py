from student import Student
from collections import Counter

class Classroom(object):
    """docstring fo Classroom."""
    def __init__(self, class_name):
        self.class_name = class_name
        self.day_time = {}
        self.students = {}
        self.students_name = []
        self.assignments = []
        self.students_grades = {}
        self.assignment_average = {}
        self.assignment_median = {}
        self.assignment_mode = {}
        print("you create the %s class" % self.class_name)

    def command(self):
        """command interface"""
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
        """add class date and time"""
        day = input("When is the %s class: " % self.class_name)
        self.day_time[day] = input("What time does it start on %s: " % day)
        more_day = input("Do you add other days? (yes or no): ")
        print(self.day_time)
        if more_day == "yes":
            self.add_class_schedule()
        else:
            return

    def remove_class_schedule(self):
        """remove class date"""
        day = input("What date do you want to remove? The class schedule is now %s: " % self.day_time)
        if day in self.day_time:
            self.day_time.pop(day)
            print("%s has been removed from the %s class" % (day, self.class_name))
            print("Now the schedule of the %s class is %s" % (self.class_name, self.day_time))
        else:
            return

    def calculate_average_grade(self):
        """calculate grade average of each student"""
        for student in self.students:
            if self.students[student].assignment_grade == {}:
                self.students_grades[student] = 0.0
            else:
                total_grade = self.students[student].total_grade
                for item in self.students[student].assignment_grade:
                    if self.students[student].assignment_grade[item] != "absent":
                        total_grade += self.students[student].assignment_grade[item]
                average = total_grade/(len(self.students[student].assignment_grade) - self.students[student].excused_absent)
                self.students_grades[student] = round(average, 2)
        print(self.students_grades)

    def add_student(self):
        """add studnet with name and time"""
        name = input("Who will you add to the %s class: " % self.class_name)
        on_time = input("He/She join in the %s class on time or late?: " % self.class_name)
        self.students[name] = Student(name, on_time)
        print("%s has been added to the %s class" % (name, self.class_name))
        if on_time == "late":
            print("%s joined in the %s class late" % (name, self.class_name))
        elif on_time != "on time":
            return 0
        self.students_name.append(name)
        print("%s has %s" % (self.class_name, self.students_name))

    def remove_student(self):
        """remove student"""
        name = input("Who will you remove from the %s class: " % self.class_name)
        if name in self.students_name:
            self.students.pop(name)
            self.students_name.remove(name)
            print("%s has been removed from the %s class" % (name, self.class_name))
            print("Now %s has %s" % (self.class_name, self.students_name))
        else:
            return

    def add_assignment(self):
        """add assignment and grade for each student"""
        assignment = input("What is the assignment name: ")
        print("you give students %s for assignment" % assignment)
        for student in self.students:
            grade = input("%s's %s grade: " % (student, assignment))
            if grade == 'absent':
                self.students[student].assignment_grade[assignment] = grade
                self.students[student].excused_absent += 1
            elif grade.isdigit() is True:
                self.students[student].assignment_grade[assignment] = int(grade)
            else:
                print("Type digit or 'absent'! Try again.")
                return
        if assignment not in self.assignments:
            self.assignments.append(assignment)

    def remove_assignment(self):
        """remove assignment"""
        all_or_one = input("Do you want to remove an assignment from all students' lists or just one student's list? (type all or one): ")
        if all_or_one == "all":
            assignment = input("Which assignment do you remove? %s: " % (self.assignments))
            self.assignments.remove(assignment)
            for student_name in self.students_name:
                if assignment in self.students[student_name].assignment_grade:
                    if self.students[student_name].assignment_grade[assignment] == "absent":
                        self.students[student_name].excused_absent -= 1
                    else:
                        pass
                    self.students[student_name].assignment_grade.pop(assignment)
                    print("%s has been removed from %s's assignment lists" % (assignment, student_name))
                else:
                    pass
        elif all_or_one == "one":
            name = input("Whose assignment do you remove: ")
            if name in self.students_name:
                assignment = input("Which assignment do you remove? %s has %s: " % (name, self.students[name].assignment_grade))
                if assignment in self.students[name].assignment_grade:
                    if self.students[name].assignment_grade[assignment] == "absent":
                        self.students[name].excused_absent -= 1
                    else:
                        pass
                    self.students[name].assignment_grade.pop(assignment)
                    print("%s has been removed from %s's assignment lists" % (assignment, name))
                else:
                    pass
        else:
            return

    def each_assignment_average(self, assignment):
        """calculate average for each assignment"""
        total = 0
        number_of_students = 0
        for student in self.students:
            if assignment in self.students[student].assignment_grade:
                if self.students[student].assignment_grade[assignment] != "absent":
                    total += self.students[student].assignment_grade[assignment]
                    number_of_students += 1
        average = total/number_of_students
        self.assignment_average[assignment] = round(average, 2)

    def each_assignment_median(self, assignment):
        """calculate median for each assignment"""
        assignment_grade_roster = []
        number_of_students = 0
        for student in self.students:
            if assignment in self.students[student].assignment_grade:
                if self.students[student].assignment_grade[assignment] != "absent":
                    assignment_grade_roster.append(self.students[student].assignment_grade[assignment])
                    number_of_students += 1
        assignment_grade_roster.sort()
        middle = number_of_students / 2
        if number_of_students % 2 != 0:
            self.assignment_median[assignment] = assignment_grade_roster[int(middle - .5)]
        else:
            middle_number = (assignment_grade_roster[int(middle - 1)] + assignment_grade_roster[int(middle)])/2
            self.assignment_median[assignment] = round(middle_number, 2)

    def each_assignment_mode(self, assignment):
        """calculate mode for each assignment"""
        assignment_grade_roster = []
        for student in self.students:
            if assignment in self.students[student].assignment_grade:
                if self.students[student].assignment_grade[assignment] != "absent":
                    assignment_grade_roster.append(self.students[student].assignment_grade[assignment])
        c = Counter((assignment_grade_roster))
        numberList = [x for x in c if c.get(x) > 1]
        if numberList == []:
            self.assignment_mode[assignment] = "none"
        else:
            i = 1
            while i < 100:
                numberList = [x for x in c if c.get(x) > i]
                if numberList == []:
                    numberList = [x for x in c if c.get(x) > (i - 1)]
                    self.assignment_mode[assignment] = numberList
                    break
                else:
                    i += 1

    def average_median_mode(self):
        """print average, median and mode"""
        assignment = input("Which assignment detail do you want to see? %s: " % self.assignments)
        self.each_assignment_average(assignment)
        self.each_assignment_median(assignment)
        self.each_assignment_mode(assignment)
        print("mean: %s, median: %s, mode: %s" % (self.assignment_average[assignment], self.assignment_median[assignment], self.assignment_mode[assignment]))

    def see_class_detail(self):
        """print class detail"""
        print("This class is " + self.class_name)
        print(self.day_time)
        print(self.assignments)
        print(self.students_grades)
        for name in self.students_name:
            print("%s %s" % (name, self.students[name].assignment_grade))
        for assignment in self.assignments:
            self.each_assignment_average(assignment)
            self.each_assignment_median(assignment)
            self.each_assignment_mode(assignment)
            print("%s: mean: %s, median: %s, mode: %s" % (assignment, self.assignment_average[assignment], self.assignment_median[assignment], self.assignment_mode[assignment]))
