arr = [3, 8, 2, 5, 1, 22, 7, 0, 15]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
print(arr)
