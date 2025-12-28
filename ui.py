from random import choice

from service import Service


class Ui:
    def __init__(self,service:Service):
        self.service=service
    def print_menu(self):
        print("1.Afiseaza studenti")
        print("2.Adauga student")
    def run_menu(self):
        while True:
            self.print_menu()
            choice=int(input("Alege varianta:"))
            if choice==1:
                students=self.service.get_students()
                for student in students:
                    print(student)
            elif choice==2:
                cnp=input("Scrie cnp:")
                nume=input("Scrie numele:")
                grupa=input("Scrie grupa studentului:")
                self.service.add_student(cnp,grupa,nume)

