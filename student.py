class Student:
    def __init__(self,cnp,grupa,nume):
        self.cnp=cnp
        self.grupa=grupa
        self.nume=nume
    def get_cnp(self):
        return self.cnp
    def get_grupa(self):
        return self.grupa
    def get_nume(self):
        return self.nume
    def set_cnp(self,cnp):
        self.cnp=cnp
    def set_grupa(self,grupa):
        self.grupa=grupa
    def set_nume(self,nume):
        self.nume=nume

    def __str__(self):
        return f"{self.get_cnp()} {self.get_nume()}: {self.get_grupa()}"



