arr = [7,2,8,5,3,22,48]

def InsertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

if __name__ == "__main__":
    InsertionSort(arr)
    for i in arr:
        print(i)