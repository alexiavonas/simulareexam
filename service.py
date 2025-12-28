from repository import Repository
from student import Student


class Service:
    def __init__(self,repository:Repository):
        self.repository=repository
    def add_student(self,cnp,grupa,nume):
        new_student=Student(cnp,grupa,nume)
        self.repository.add_student(new_student)
    def get_students(self):
        return self.repository.get_students()


