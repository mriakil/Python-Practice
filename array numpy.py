from numpy import *

arr1 = array([0,78,45,64,90])
arr2 = array([2,6,3,11,42])



print(concatenate([arr1,arr2]))


arr = array([13,135,21,52])
arr3 = arr.copy

arr[1] = 8

print(arr)
print(arr3)

print(id(arr))
print(id(arr3))