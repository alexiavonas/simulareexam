
class Error(Exception):
    pass
class StudentValidator():
    def validate(self,cnp):
        if not cnp>100:
            raise Error("Cnp invalid")
