import math 
#Non-Divisible Subset
'''
Given a set of distinct integers, print the size of a maximal subset of S
where the sum of any 2 numbers in S` is not evenly divisible by k.
'''
def nonDivisibleSubset(k, s):
    count = 0
    remainders = [0] * k
    for n in s:
        r = n % k
        remainders[r] += 1
    if remainders[0] > 0:
        count += 1
    for i in range(1, math.ceil(k / 2)):
        count += max(remainders[i], remainders[-i])
    if k % 2 == 0:
        index = int(k / 2)
        if remainders[index] > 0:
            count += 1
    return count
