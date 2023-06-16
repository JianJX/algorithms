def mergeSort(arr):
    total = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        total += mergeSort(left)
        total += mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                print(left[i], right[j], (len(left) - i))
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

m = [38, 27, 43, 3, 9, 82, 10]
n = [1, 1, 1, 2, 2]
p = [3, 5, 7, 11, 9]
a = mergeSort(p)
print(a)