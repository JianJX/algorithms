#Insertion Sort Advanced Analysis
'''
Insertion Sort is a simple sorting technique which was covered in
previous challenges. Sometimes, arrays may be too large for us to 
wait around for insertion sort to finish. Is there some other way 
we can calculate the number of shifts an insertion sort performs 
when sorting an array?
'''
def insertionSort(arr):
    total = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        total += insertionSort(left)
        total += insertionSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                total += (len(left) - i)
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        total = 0
    return total

