class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num<=10:

            val = self.num
            self.num += 1
            return val

        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)

#Generators

def square():

    n = 1

    while n<=10:
        sq = n*n
        yield sq
        n += 1

val = square()
for i in val:
    print(i)


#Exceptions

a = 5
b = 3

try:
    print(a/b)
    k = int(input("Enter an Integer : "))
    print(k)

except ZeroDivisionError as e :
    print("Can't be divided by Zero", e)

except ValueError as e :
    print("It is not an Integer", e)
except Exception as e:
    print("Error Happened", e)

finally:
    print("You got your answer Right?")

print("Bye")