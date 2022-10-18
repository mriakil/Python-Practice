

class PyCharm:

    def execute(self):
        print("Computing")
        print("Runing")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Conversion Check")
        print("Computing")
        print("Runing")

class Laptop:

    def code(self,ide):
        ide.execute()


ide = MyEditor()


lap1 = Laptop()
lap1.code(ide)