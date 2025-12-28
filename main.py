from repository import Repository
from service import Service
from ui import Ui

if __name__=='__main__':
    repository=Repository()
    service=Service(repository)
    ui=Ui(service)
    ui.run_menu()