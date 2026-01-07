class Student(object):
    def __init__(self, first, last, age):
        self.__name = first
        self.__surname = last
        self.__age = age
    def getName(self):
        return self.__name

if __name__ == "__main__":
    aStudent = Student("John", "Doe", 21)
    nm = aStudent.getName()
    nm = aStudent.name
    print(nm)