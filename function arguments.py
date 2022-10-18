

#def person(name, age=18):
 #   print(name)
  #  print(age)


#person('AKIL', 22)


def sum(*b):
    c= 0

    for i in b:
        c= c+ i

    print(c)

sum(8,25,21,56)


def person(name, **data):
    print("Name:", name)
    print(data)

    for i, j in data.items():
        print(i,j)

person("AKIL", age=22, city="Chittagong", mob=+8801832103527)


a = 10
print(id(a))
print(a)
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("in function" , a)
    globals()['a'] = 18

something()

print("outside", a)