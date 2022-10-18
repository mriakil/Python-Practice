from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.3)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi!")
            sleep(0.3)

class Goodbye(Thread):
    def run(self):
        for i in range(5):
            print("Goodbye")
            sleep(0.3)


t1 = Hello()
t2 = Hi()
t3 = Goodbye()

t1.start()
sleep(0.0000001)
t2.start()
sleep(0.000001)
t3.start()

t1.join()
t2.join()
t3.join()
print("Bye")