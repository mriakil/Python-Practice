class student:
    def __init__(self, name, rollno):
        self.n = name
        self.r = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.n, self.r )
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 6

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student("Akil", 3)
s2 = student("Raisul", 1)

s1.show()


