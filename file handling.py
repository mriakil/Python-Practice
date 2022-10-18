
f = open('MyData', 'r')
f2 = open('MyData', 'a')

print(f.read())

f2.write("I think now i can edit it properly")




f1 = open("abc", 'w')
f1.write("This is how i can create a file and write something on it")
f1.write("I can edit it from here too")

for data in f:
    f1.write(data)