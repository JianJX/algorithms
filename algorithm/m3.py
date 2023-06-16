#Queen's Attack II
'''
You will be given a square chess board with one queen and a number of obstacles placed on it. 
Determine how many squares the queen can attack.
'''
def queensAttack(n, k, r_q, c_q, obstacles):
    moves = 0
    ob_list = [ ]
    for i in range(8):
        ob_list.append([])
    for obstacle in obstacles:
        row = obstacle[0]
        col = obstacle[1]
        if row == r_q and col < c_q:#left
            ob_list[0].append(c_q - col - 1)
        elif row == r_q and col > c_q:#right
            ob_list[1].append(col - c_q - 1)
        elif col == c_q and row < r_q:#down
            ob_list[2].append(r_q - row - 1)
        elif col == c_q and row > r_q:#up
            ob_list[3].append(row - r_q - 1)
        elif (row - r_q) == (col - c_q) and row > r_q and col > c_q:#up right
            ob_list[4].append(row - r_q - 1)
        elif (row - r_q) == (c_q - col) and row > r_q and c_q > col:#up left
            ob_list[5].append(row - r_q - 1)
        elif (r_q - row) == (col - c_q) and r_q > row and col > c_q:#down right
            ob_list[6].append(r_q - row - 1)
        elif (r_q - row) == (c_q - col) and r_q > row and c_q > col:#down left
            ob_list[7].append(r_q - row - 1)
    for i in range(len(ob_list)):
        if ob_list[i] != []:
            moves += min(ob_list[i])
        else:
            print(i)
            if i == 0:
                moves += (c_q - 1)
            elif i == 1:
                moves += (n - c_q)
            elif i == 2:
                moves += (r_q - 1)
            elif i == 3:
                moves += (n - r_q)
            elif i == 4:
                moves += (min(n - r_q, n - c_q))
            elif i == 5:
                moves += (min(n - r_q, c_q - 1))
            elif i == 6:
                moves += (min(r_q - 1, n - c_q))
            elif i == 7:
                moves += (min(r_q - 1, c_q - 1))
    return moves