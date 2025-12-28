class Repository:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def get_students(self):
        return self.students
