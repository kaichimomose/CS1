import pytest
from student import Student

def setup_test():
    student = Student("kaichi", "on time")
    return student

def test():
    student = setup_test()
    assert student.name == "kaichi"
