

def fact(n):

    f = 1

    for i in range(1,n+1):  #5*4*3*2*1
        f = f*i

    return f

x = int(input("Enter the Number : "))

result = fact(x)

print("The factorial of", x, "! =",  result)