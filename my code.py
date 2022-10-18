x= int(input('enter 1st num'))
y=int(input('enter 2nd num'))
z=int(input('enter 3rd num'))
if x>0:
    print("X is positive")
else:
    print("X is negative")
print("See your answer below")
if x>y and x>z:
    print("X is greater")
elif y>x and y>z:
    print("Y is greater")
elif z>x and z>y:
    print("Z is greater")
else:
    print("All are equal")