

f = lambda a,b : a-b

result = f(4,8)

print(result)

from functools import reduce

nums = [2, 2, 3, 6, 4,5, 3, 9, 8]

evens = list(filter(lambda n: n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda a,b : a+b, evens)

print(evens)
print(doubles)
print(sum)