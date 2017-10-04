class Classroom(object):
    """docstring fo Classroom."""
    def __init__(self, class_name, day_time):
        self.class_name = class_name
        self.day_time = day_time
        self.students = {}
        self.assignments = []
        self.students_grades = {}

    def calculate_average_grade(self):
        for student in self.students:
            total_grade = self.students[student].total_grade
            for item in self.students[student].assignment_grade:
                total_grade += self.students[student].assignment_grade[item]
            average = total_grade/len(self.students[student].assignment_grade)
            self.students_grades[student] = round(average, 2)

    def add_student(self, name):
        self.students[name] = Student(name)
        print("%s has been added to %s" % (name, self.class_name))
        student_name = []
        for student in self.students:
            student_name.append(student)
        print("%s has %s" % (self.class_name, student_name))

    def remove_student(self, name):
        self.students.pop(name)
        print("%s has been removed from %s" % (name, self.class_name))
        student_name = []
        for student in self.students:
            student_name.append(student)
        print("Now %s has %s" % (self.class_name, student_name))

    def add_assignment(self, assignment):
        for student in self.students:
            self.students[student].assignment_grade[assignment] = int(input("%s's %s grade: " % (student, assignment)))
        if assignment not in self.assignments:
            self.assignments.append(assignment)

    def remove_assignment(self, name, assignment):
        self.students[name].assignment_grade.pop(assignment)


class Student(object):
    def __init__(self, name):
        self.name = name
        self.assignment_grade = {}
        self.total_grade = 0
        self.number_assignment = 0


math = Classroom("Math", {"Monday": "10:30"})
math.add_student("Hadou")
math.add_assignment("zookeeper")
math.add_student("Kaichi")
math.add_assignment("fizzbuzz")
math.add_student("Shin")
math.add_student("Kuze")
# math.add_assignment("Hadou", "fizzbuzz", 6)

math.remove_student("Shin")

print(math.students["Hadou"].assignment_grade)
print(math.students["Kaichi"].assignment_grade)

print(math.students)

print(math.assignments)

# math.calculate_average_grade()
# print(math.students_grades)
