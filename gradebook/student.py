class Student(object):
    def __init__(self, name, on_time):
        self.name = name
        self.on_time = on_time
        self.assignment_grade = {}
        self.total_grade = 0
        self.excused_absent = 0
