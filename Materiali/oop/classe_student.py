import string

class Student:
    '''A class representing a student.'''
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQPoints(self):
        return self.qpoints
    def gpa(self):    
        return self.qpoints/self.hours
    
prova = Student("Giovanni", 10, 20)

print (prova.__doc__)

