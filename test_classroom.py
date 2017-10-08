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
    classroom.remove_assignment("all", "Hangman", "Hadou")
    assert classroom.students["Hadou"].assignment_grade == {}
