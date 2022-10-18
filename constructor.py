"""
class Computer:
    def __init__(self):
        self.name = "Akil"
        self.age = 21


    def update(self):
        self.age = 22

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c2.age = 32
print(c2.age)

if c1.compare(c2):
    print("They are same")

else:
    print("They are different")

c1.name = "Raisul"
c2.update()



print(c1.name)
print(c2.age)

"""

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()
c2.mil = 8
Car.wheels = 6
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)