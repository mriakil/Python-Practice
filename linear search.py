
position = -1
def search(list,n):
    i = 0

    while i< len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i = i+ 1
    return False

list = [9, 2, 53, 24, 2,4,42]   #list can be random not need to arrange
n = int(input("Enter the number you want to find: "))

if search(list, n):
    print(f"Found at {n} position ", position+1)

else:
    print("Not Found")

#binary search
pos = -1
def find(numbers, m):
    l = 0
    u = len(numbers) - 1

    while l <= u:
        mid = (l+u)//2

        if numbers[mid] == m:
            globals()['pos'] = mid
            return True
        else:
            if numbers[mid] < m:
                l = mid + 1
            else:
                u = mid - 1
    return False

numbers = [2,3,5,31,39, 41, 42]    #list must be arranged gradually if upper case else lower case
m = 42

if find(numbers,m):
    print(f"Found at {m} position ", pos+1)

else:
    print("Not FOUND!!!")