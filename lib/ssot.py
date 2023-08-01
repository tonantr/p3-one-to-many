# Single Source of Truth (SSOT)

class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._teacher = None
        Student.all.append(self)

    # teacher property

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self