from StudentValidator import StudentValidator
from repository import Repository
from service import Service
from ui import Ui

if __name__=='__main__':
    repository=Repository()
    service=Service(repository)
    validator = StudentValidator()
    ui=Ui(service, validator)
    ui.run_menu()