import pytest
from classroom_for_test import Classroom


def setup_test():
    classroom = Classroom("Math")
    classroom.add_class_schedule("Monday", "10:00", "yes")
    classroom.add_class_schedule("Tuesday", "14:00", "no")
    classroom.add_student("Hadou", "on time")
    classroom.add_assignment("Hangman", "100")
    return classroom


def test__init__():
    classroom = setup_test()
    assert classroom.class_name == "Math"


def test_add_class_schedule():
    classroom = setup_test()
    assert classroom.day_time == {"Monday": "10:00", "Tuesday": "14:00"}


def test_remove_class_schedule():
    classroom = setup_test()
    classroom.remove_class_schedule("Monday")
    assert classroom.day_time == {"Tuesday": "14:00"}


def test_add_remove_student():
    classroom = setup_test()
    error = classroom.remove_student("Kaichi")
    assert error == 0
    classroom.remove_student("Hadou")
    assert classroom.students == {}
    classroom.add_student("Kaichi", "abc")
    assert error == 0


def test_add_assignment():
    classroom = setup_test()
    assert classroom.students["Hadou"].assignment_grade["Hangman"] == 100
    assert classroom.assignments == ["Hangman"]
    error = classroom.add_assignment("Hangman", "A")
    assert error == 0
    classroom.add_assignment("Zookeeper", "absent")
    assert classroom.students["Hadou"].assignment_grade["Zookeeper"] == "absent"
    assert classroom.students["Hadou"].excused_absent == 1


def test_remove_assingment():
    classroom = setup_test()
    classroom.add_assignment("Fizzbuzz", "absent")
    assert classroom.students["Hadou"].excused_absent == 1
    classroom.remove_assignment("one", "Fizzbuzz", "Hadou")
    assert classroom.students["Hadou"].excused_absent == 0
    classroom.remove_assignment("all", "Fizzbuzz")
    assert classroom.students["Hadou"].excused_absent == 0
    classroom.add_student("Kaichi", "late")
    assert classroom.students_name == ["Hadou", "Kaichi"]
    classroom.add_assignment("Zookeeper", "20")
    assert classroom.students["Kaichi"].assignment_grade == {"Zookeeper": 20}
    assert classroom.students["Hadou"].assignment_grade == {"Hangman": 100, "Zookeeper": 20}
    assert classroom.assignments == ["Hangman", "Zookeeper"]
    classroom.remove_assignment("all", "Zookeeper")
    assert classroom.assignments == ["Hangman"]
    assert classroom.students["Hadou"].assignment_grade == {"Hangman": 100}
    assert classroom.students["Kaichi"].assignment_grade == {}
    classroom.remove_assignment("one", "Hangman", "Hadou")
    assert classroom.students["Hadou"].assignment_grade == {}
    error = classroom.remove_assignment("al", "Zookeeper")
    assert error == 0


def test_calculate_average_grade():
    classroom = setup_test()
    classroom.add_assignment("Zookeeper", "20")
    classroom.add_assignment("Fizzbuzz", "absent")
    assert classroom.students["Hadou"].assignment_grade == {"Hangman": 100, "Zookeeper": 20, "Fizzbuzz": "absent"}
    classroom.calculate_average_grade()
    assert classroom.students["Hadou"].excused_absent == 1
    assert classroom.students_grades == {"Hadou": 60.0}


def test_command():
    classroom = setup_test()
    classroom.command("as")
    assert classroom.students_name == ["Hadou", "Chris"]
    classroom.command("rs")
    assert classroom.students_name == ["Chris"]
    classroom.command("aa")
    assert classroom.students["Chris"].assignment_grade == {"Fizzbuzz": 50}
    classroom.command("ra")
    assert classroom.students["Chris"].assignment_grade == {}
    classroom.command("ac")
    assert classroom.day_time == {"Monday": "10:00", "Tuesday": "14:00", "Thursday": "16:00"}
    classroom.command("rc")
    assert classroom.day_time == {"Tuesday": "14:00", "Thursday": "16:00"}
    classroom.command("c")
    assert classroom.students_grades == {"Chris": 0.0}
    exit = classroom.command("e")
    assert exit == 0


def test_assignment_average_median_mode():
    classroom = setup_test()
    classroom.add_student("Kaichi0", "late")
    classroom.add_student("Kaichi1", "late")
    classroom.add_student("Kaichi2", "late")
    classroom.add_student("Kaichi3", "late")
    classroom.add_student("Kaichi4", "late")
    classroom.add_assignment_each("Kaichi0", "Hangman", "30")
    assert classroom.students["Kaichi0"].assignment_grade == {"Hangman": 30}
    classroom.add_assignment_each("Kaichi1", "Hangman", "50")
    classroom.add_assignment_each("Kaichi2", "Hangman", "30")
    classroom.add_assignment_each("Kaichi3", "Hangman", "20")
    classroom.add_assignment_each("Kaichi4", "Hangman", "30")
    classroom.each_assignment_average("Hangman")
    assert classroom.assignment_average == {"Hangman": 43.33}
    classroom.each_assignment_median("Hangman")
    assert classroom.assignment_median == {"Hangman": 30.00}
    classroom.add_assignment_each("Hadou", "Zookeeper", "24")
    classroom.add_assignment_each("Kaichi0", "Zookeeper", "39")
    classroom.add_assignment_each("Kaichi1", "Zookeeper", "60")
    classroom.add_assignment_each("Kaichi2", "Zookeeper", "40")
    classroom.add_assignment_each("Kaichi3", "Zookeeper", "20")
    classroom.add_assignment_each("Kaichi4", "Zookeeper", "30")
    classroom.each_assignment_average("Zookeeper")
    assert classroom.assignment_average == {"Hangman": 43.33, "Zookeeper": 35.50}
    classroom.add_student("Kaichi5", "late")
    classroom.add_assignment_each("Kaichi5", "Zookeeper", "55")
    classroom.each_assignment_median("Zookeeper")
    assert classroom.assignment_median == {"Hangman": 30.00, "Zookeeper": 39.00}
    classroom.each_assignment_mode("Hangman")
    assert classroom.assignment_mode == {"Hangman": [30]}
    classroom.each_assignment_mode("Zookeeper")
    assert classroom.assignment_mode == {"Hangman": [30], "Zookeeper": "none"}
    classroom.add_assignment_each("Hadou", "Fizzbuzz", "20")
    classroom.add_assignment_each("Kaichi0", "Fizzbuzz", "20")
    classroom.add_assignment_each("Kaichi1", "Fizzbuzz", "20")
    classroom.add_assignment_each("Kaichi2", "Fizzbuzz", "30")
    classroom.add_assignment_each("Kaichi3", "Fizzbuzz", "30")
    classroom.add_assignment_each("Kaichi4", "Fizzbuzz", "30")
    classroom.add_assignment_each("Kaichi5", "Fizzbuzz", "55")
    classroom.each_assignment_mode("Fizzbuzz")
    assert classroom.assignment_mode == {"Hangman": [30], "Zookeeper": "none", "Fizzbuzz": [20, 30]}
    classroom.add_assignment_each("Hadou", "Gradebook", "20")
    classroom.add_assignment_each("Kaichi0", "Gradebook", "20")
    classroom.add_assignment_each("Kaichi1", "Gradebook", "20")
    classroom.add_assignment_each("Kaichi2", "Gradebook", "30")
    classroom.add_assignment_each("Kaichi3", "Gradebook", "absent")
    classroom.add_assignment_each("Kaichi4", "Gradebook", "absent")
    classroom.add_assignment_each("Kaichi5", "Gradebook", "55")
    classroom.each_assignment_mode("Gradebook")
    assert classroom.assignment_mode == {"Hangman": [30], "Zookeeper": "none", "Fizzbuzz": [20, 30], "Gradebook": [20]}
    classroom.each_assignment_average("Gradebook")
    assert classroom.assignment_average["Gradebook"] == 29.00
    classroom.each_assignment_median("Gradebook")
    assert classroom.assignment_median["Gradebook"] == 20.00
