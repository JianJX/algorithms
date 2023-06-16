#Forming a Magic Square
'''
We define a magic square to be an n x n matrix of distinct positive integers
from 1 to n^2 where the sum of any row, column, or diagonal of length n is
always equal to the same number: the magic constant.
'''
def formingMagicSquare(s):
    costs = [ ]
    magic = [[8, 3, 4, 9, 2, 7, 6, 1],
            [4, 9, 2, 7, 6, 1, 8, 3],
            [2, 7, 6, 1, 8, 3, 4, 9],
            [6, 1, 8, 3, 4, 9, 2, 7],
            [8, 1, 6, 7, 2, 9, 4, 3],
            [4, 3, 8, 1, 6, 7, 2, 9],
            [2, 9, 4, 3, 8, 1, 6, 7],
            [6, 7, 2, 9, 4, 3, 8, 1]]
    square = [s[0][0], s[0][1], s[0][2], s[1][2],
             s[2][2], s[2][1], s[2][0], s[1][0]]
    for m in magic:
        total = 0
        for i in range(len(m)):
            total += abs(m[i] - square[i])
        total += abs(5 - s[1][1])
        costs.append(total)
    for m in magic:
        total = 0
        for i in range(len(m)):
            total += abs(m[i] - square[i])
        total += abs(5 - s[1][1])
        costs.append(total)
    return min(costs)