import pytest
from school_for_test import School


def setup_test():
    school = School()
    school.creat_classes('yes', 'CS1')
    return school


def test_creat_classes():
    school = setup_test()
    assert school.class_roster == ["CS1"]
    assert school.class_rooms["CS1"].day_time == {'Monday': '10:00'}
    assert school.class_rooms["CS1"].students_name == ["Chris"]
    school.creat_classes('no', 'CS1')
    assert school.class_rooms["CS1"].day_time == {}
