import pytest
from classroom_for_test import Classroom
from student import Student


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


def test_add_assignment():
    classroom = setup_test()
    assert classroom.students["Hadou"].assignment_grade["Hangman"] == 100
    assert classroom.assignments == ["Hangman"]
    error = classroom.add_assignment("Hangman", "A")
    assert error == 0


def test_remove_assingment():
    classroom = setup_test()
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
    classroom.calculate_average_grade()
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
