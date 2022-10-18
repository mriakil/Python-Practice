

def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i % 2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst =[20,42,33,110,49,92, 49, 23, 49,28,23]
even,odd =count(lst)
print("Even :", even)
print("Odd :", odd)

print("Even : {} and Odd : {}".format(even,odd))


