def binarySearch(array, target, left, right):
    if (left > right):
        return False
    mid = (left + right)// 2
    if (array[mid] == target):
        return True
    elif(target < array[mid]):
        return binarySearch(array, target, left, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, right)


array = [2,45,52,88,4,5,8,24,92,7,99,72]
target = int(input("Enter element : "))
left, right = 0, len(array) - 1
res = binarySearch(array, target, left, right)
if res == True:
    print('Element found')
else:
    print('Element not found')