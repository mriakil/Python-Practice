#num = 97
#for i in range(2,num):
 #   if num % i == 0:
  #      print("Not prime")
   #     break
#else:
 #   print("prime")

def isPrime(n):
    if (n<=1):
        return False
    for i in range(2,n):
        if ( n%i ==0):
            return False
    return True
if isPrime(87):
    print ("Prime Number")
else:
    print("Not Prime Number")
