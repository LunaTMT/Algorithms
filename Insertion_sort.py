def insertionSort(arr):
     
    if (n := len(arr)) <= 1:
      return
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
    
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def insertionSortRecusive(arr, n):
    if n <= 1:
        return
    
    insertionSortRecusive(arr, n-1)
    last = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j+1] = last
 

arr = [4, 3, 5, 0, 1]
insertionSort(arr)
print(arr)
