from student import Student
from collections import Counter
import matplotlib.pyplot as plt



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
                    if self.students[student].assignment_grade[item] != "absent":
                        total_grade += self.students[student].assignment_grade[item]
                average = total_grade/(len(self.students[student].assignment_grade) - self.students[student].excused_absent)
                self.students_grades[student] = round(average, 2)
        print(self.students_grades)

    def add_student(self, name, on_time):
        name = name
        on_time = on_time
        self.students[name] = Student(name, on_time)
        print("%s has been added to the %s class" % (name, self.class_name))
        if on_time == "late":
            print("%s joined in the %s class late" % (name, self.class_name))
        elif on_time != "on time":
            return 0
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
            if grade == 'absent':
                self.students[student].assignment_grade[assignment] = grade
                self.students[student].excused_absent += 1
            elif grade.isdigit() is True:
                self.students[student].assignment_grade[assignment] = int(grade)
            else:
                print("Type digit or 'absent'! Try again.")
                return 0
        if assignment not in self.assignments:
            self.assignments.append(assignment)

    def add_assignment_each(self, student, assignment, grade):
        assignment = assignment
        grade = grade
        if grade == 'absent':
            self.students[student].assignment_grade[assignment] = grade
            self.students[student].excused_absent += 1
        elif grade.isdigit() is True:
            self.students[student].assignment_grade[assignment] = int(grade)
        else:
            print("Type digit or 'absent'! Try again.")
            return 0
        if assignment not in self.assignments:
            self.assignments.append(assignment)
            print("you give students %s for assignment" % assignment)

    def remove_assignment(self, all_or_one, assignment, name=""):
        all_or_one = all_or_one
        if all_or_one == "all":
            assignment = assignment
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
            name = name
            if name in self.students_name:
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
            return 0

    def each_assignment_average(self, assignment):
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

    def see_class_detail(self):
        print("This class is " + self.class_name)
        print(self.day_time)
        print(self.assignments)
        print(self.students_grades)
        for name in self.students_name:
            print("%s: %s" % (name, self.students[name].assignment_grade))

    def show_assignment_average_graph(self):
        plt.bar(self.assignment_average.keys(), self.assignment_average.values(), align='center', alpha=0.5)
        plt.ylabel('average points')
        plt.xlabel('assignments')
        plt.title('Mean of each assignment', fontsize=20, color='black')
        plt.show()

    def show_assignment_median_graph(self):
        plt.bar(self.assignment_median.keys(), self.assignment_median.values(), align='center', alpha=0.5)
        plt.ylabel('median points')
        plt.xlabel('assignments')
        plt.title('Median of each assignment', fontsize=20, color='black')
        plt.show()

    def show_students_grades_graph(self):
        plt.bar(self.students_grades.keys(), self.students_grades.values(), align='center', alpha=0.5)
        plt.ylabel('average points')
        plt.xlabel('students')
        plt.title("Mean of each student's grade", fontsize=20, color='black')
        plt.show()

    def show_number_of_excused_absent_graph(self):
        students_name = []
        number_of_excused_absent = []
        for student in self.students:
            students_name.append(student)
            number_of_excused_absent.append(self.students[student].excused_absent)
        plt.bar(students_name, number_of_excused_absent, align='center', alpha=0.5)
        plt.ylabel('number of excused absent')
        plt.xlabel('students')
        plt.title("Number of excused absent of each student", fontsize=20, color='black')
        plt.show()
