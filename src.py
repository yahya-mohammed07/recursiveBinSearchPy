import math

# the array needs to be sorted
arr = [1,2,3,4,5,6,7,8,9,10]
# assigning length to a local var to a void calling len
size = len(arr)
low = 0
high = size - 1
# the user enter the target to search
target = int(input("enter a number to search: "))
# the recursive bin search
def binSearch (arr, low, high, size, target):
    mid = (int)(math.ceil(low + high) / 2)
    if high >= low:
        if arr[mid] == target:
            print("found at index ", mid)
            return 1
        elif target > arr[mid]:
            return binSearch(arr, low + 1, high, size, target)
        else:
            return binSearch(arr, low, high - 1, size, target)
    print("not found")
    return 0

# calling the function
binSearch(arr, low, high, size, target)