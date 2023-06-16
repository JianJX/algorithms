def recur(arr, c_arr, n, A):
    for i in A:
        if n / i == 1:
            c_arr.append(c_arr[-1] * i)
            arr.append(c_arr)
            return 0
        elif n % i == 0:
            new_arr = [ ]
            for num in c_arr:
                new_arr.append(num)
            new_arr.append(new_arr[-1] * i)
            recur(arr, new_arr, n / i, A)

def kFactorization(n, A):
    arr = [ ]
    A.sort(reverse=True)
    for i in A:
        if n % i == 0:
            recur(arr, [1, i], n / i, A)
    if arr == []:
        return [-1]
    arr_lens = [ ]
    for ar in arr:
        arr_lens.append(len(ar))
    smallest_arr = []
    for ar in arr:
        if len(ar) == min(arr_lens):
            smallest_arr.append(ar)
    return min(smallest_arr)

print(kFactorization(231000000, [2,3,5,7,11,13,17,19]))