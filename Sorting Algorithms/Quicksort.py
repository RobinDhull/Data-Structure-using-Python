import random
def quickSort(array, left, right):
    if (left >= right):
        return
    pivot = array[random.randint(left, right)]
    index = partition(array, left, right, pivot)
    quickSort(array, left, index - 1) 
    quickSort(array, index, right)

def partition(array, left, right, pivot):
    while (left <= right):
        while (array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        
        if (left <= right):
            array[left], array[right] = array[right], array[left]   
            left += 1
            right -= 1
    return left

array = [3, 8, 2, 5, 1, 22, 7, 0, 15]
left, right = 0, len(array) - 1
quickSort(array, left, right)
for i in array:
    print(i) 
    

