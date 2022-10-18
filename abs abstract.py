from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def work(self):
        pass



class Desktop:
    def process(self,com):
        print("its from Desktop")
        com.work()

class Debugger():
    def work(self):
        print("Solving Bugs")


class Programmer():
    def work(self):
        print("Finding Bugs")


class Laptop():
    def process(self,com):
        print("its from Laptop")
        com.work()

com1 = Laptop()
com2 = Desktop()
prog1 = Programmer()
prog2 = Debugger()


com2.process(prog1)
com1.process(prog2)
