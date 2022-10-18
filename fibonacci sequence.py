
#flag_bangladesh
from turtle import *
penup()
goto(-150,-100)
pendown()
color("green")
begin_fill()
for i in[500,300]*2:
    forward(i)
    circle(30,90)
end_fill()

penup()
goto(90,-20)
pendown()
begin_fill()
color("red")
circle(100)
end_fill()
hideturtle()
done()


#
x = 0

def fib(n):
    a = 0
    b = 1

    if n == 1 :
        print(a)

    elif n <=0:
        print("Not Possible")


    else:

        print(a)
        print(b)

        for i in range(2,n):
            global x
            x += 1
            c = a+b
            a = b
            b= c
            if c>50:
                break
            print(c, x)
    print("Total fibonacci number is ", x+1)

fib(20)

#