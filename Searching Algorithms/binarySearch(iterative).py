def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if (array[mid] == target):
            return True
        elif (target < array[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return False

array = [2,45,52,88,4,5,8,24,92,7,99,72]
target = int(input("Enter element : "))
res = binarySearch(array, target)
if res == True:
    print('Element found')
else:
    print('Element not found')
    