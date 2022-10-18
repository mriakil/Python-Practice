
class Student:

    school = "XYZ School"

    def __init__(self, math, english, m3):
        self.math = math
        self.m2 = english
        self.bangla = m3

    def avg(self):
        return (self.math + self.m2 + self.bangla)/3

    @classmethod
    def getschool(cls):
        return cls.school

    def info():
        print("This is student class... in abc module")

s1 = Student(34,24,64)
s2 = Student(43,76,78)

print(s1.math)
print(s2.m2)
print(s1.bangla)


print(s1.avg())
print(s2.avg())
print(Student.getschool())
Student.info()