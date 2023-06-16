import math

def form_longest_palindrome(s):
    d = {}
    result = ''
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    while True:
        cond = False
        for key in d:
            if d[key] > 1:
                cond = True
                d[key] -= 2
                result += key
        if cond == False:
            copy = result[::-1]
            for key in d:
                if d[key] == 1:
                    result += key
                    break
            result += copy
            break
    return result

def pair_sum_count(a, m, k):
    count = 0
    for i in range(len(a)):
        if (len(a) - i) > (m - 1):
            sub_array = []
            for j in range(m):
                sub_array.append(a[i + j])
            firstMax = max(sub_array)
            sub_array.remove(firstMax)
            secondMax = max(sub_array)
            if (firstMax + secondMax) >= k:
                count += 1
    return count

def get_min_cost(cntProducts, quantities, costs, meals):
    num_stores = len(quantities)
    min_cost_list = []
    for meal in meals:
        store_index = 0
        count = 0
        total_cost_list = []
        while store_index != (num_stores - 1):
            for i in range(store_index + 1, num_stores):
                total_cost = 0
                cond = True
                for j in range(cntProducts):
                    require_quantity = meal[j]
                    if (quantities[store_index][j] + quantities[i][j]) >= require_quantity: #if both stores have enough
                        if costs[store_index][j] < costs[i][j]: #store1 first as it is cheaper
                            if require_quantity > quantities[store_index][j]: #store1 doesn't have enough, buy from both stores
                                total_cost += (costs[store_index][j] * quantities[store_index][j])
                                require_quantity -= quantities[store_index][j]
                                total_cost += (costs[i][j] * require_quantity)
                            else: #store1 has enough, only buy from store1
                                total_cost += (costs[store_index][j] * require_quantity)
                        elif costs[store_index][j] > costs[i][j]: #store2 first as it is cheaper
                            if require_quantity > quantities[i][j]: #store2 doesn't have enough, buy from both stores
                                total_cost += (costs[i][j] * quantities[i][j])
                                require_quantity -= quantities[i][j]
                                total_cost += (costs[store_index][j] * require_quantity)
                            else: #store2 has enough, only buy from store1
                                total_cost += (costs[i][j] * require_quantity)
                        else: #same price doesn't matter
                            total_cost += (costs[i][j] * require_quantity)
                    else:
                        cond = False
                        break
            if cond:
                total_cost_list.append(total_cost)
            store_index += 1
        min_cost = min(total_cost_list)
        min_cost_list.append(min_cost)
    return min_cost_list

def extract_palindrome_prefix(s):
    for i in range(len(s)):
        st = s[0:len(s) - i]
        if len(st) > 1:
            if st == st[::-1]:
                return extract_palindrome_prefix(s[len(s) - i:])
    return s

def boolean_arr(numbers, left, right):
    result = []
    for i in range(len(numbers)):
        n = numbers[i] / (i + 1)
        if numbers[i] % (i + 1) != 0:
            result.append(False)
        else:
            if n <= right and n >= left:
                result.append(True)
            else:
                result.append(False)
    return result

def solution(a):
    result = []
    d = {}
    for num in a:
        num_str = str(num)
        for i in range(len(num_str)):
            if num_str[i] in d:
                d[num_str[i]] += 1
            else:
                d[num_str[i]] = 1
    most = d[max(d, key=d.get)]
    for key in d:
        if d[key] == most:
            result.append(int(key))
    result.sort()
    return result

def solution(n, lights):
    arr = lights
    '''
    for light in lights: 
        location = light[0]
        radius = light[1]
        left_cover = location - radius
        right_cover = location + radius
        if left_cover < 0:
            left_cover = 0
        if right_cover > n:
            right_cover = n
        arr.append([left_cover, right_cover])
    '''
    arr.sort()
    if arr[0][0] > 0 or arr[-1][1] < n:
        return -1
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i][0] <= result[-1][0] and arr[i][1] > result[-1][1]:
            result.pop(-1)
            result.append(arr[i])
        elif arr[i][0] <= result[-1][1] and arr[i][1] > result[-1][1]:
            result.append(arr[i])
    return len(result)    

lights = [[0,3],[2,7],[4,8],[0,1],[7,10],[6,8]]
r = solution(10, lights)

def solution(a, k):
    rib_len = max(a)
    while True:
        num_rib = 0
        for n in a:
            num_rib += (n // rib_len)
        if num_rib == k:
            return rib_len
        else:
            rib_len -= 1


def possible_ways_by_remove_digit(s, t):
    count = 0
    for i in range(len(s)):
        if ord(s[i]) <= 57 and ord(s[i]) >= 48:
            new_s = s[0:i] + s[i + 1:]
            if new_s < t:
                count += 1
    for j in range(len(t)):
        if ord(t[j]) <= 57 and ord(t[j]) >= 48:
            new_t = t[0:j] + t[j + 1:]
            if s < new_t:
                count += 1
    return count

def count_subarray_sum(arr, k, s):
    count = 0
    for i in range(len(arr)):
        for j in range(k):
            if (j + i) < len(arr):
                sub_arr = arr[i:i + j + 1]
                if sum(sub_arr) == s:
                    count += 1
    return count

def solution(preferences):
    f1 = preferences[0]
    f2 = preferences[1]
    f3 = preferences[2]
    for i in range(len(f1)):
        most = max(f1[i], f2[i], f3[i])
        print(most)
#Hard
def get_maximum_apple(row, col, count, matrix):
    if matrix[row][col] == 1:
        count += 1
    if (row + 1) < len(matrix) and (col + 1) < len(matrix[0]):
        return max(get_maximum_apple(row + 1, col, count, matrix),
        get_maximum_apple(row, col + 1, count, matrix))
    elif (row + 1) < len(matrix):
        return get_maximum_apple(row + 1, col, count, matrix)
    elif (col + 1) < len(matrix[0]):
        return get_maximum_apple(row, col + 1, count, matrix)
    elif row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return count


#Medium
def group_arr_by_mean(a):
    result = []
    for i in range(len(a)):
        mean = sum(a[i]) / len(a[i])
        group_index = -1
        for j in range(len(result)):
            arr_mean = sum(a[result[j][0]]) / len(a[result[j][0]])
            if arr_mean == mean:
                group_index = j
                break
        if group_index == -1:
            result.append([i])
        else:
            result[group_index].append(i)
    return result

#optimization needed
def occurrence_in_sub_arr(a, queries):
    result = 0
    for q in queries:
        left = q[0]
        right = q[1]
        x = q[2]
        arr = a[left:right + 1]
        for n in arr:
            if n == x:
                result += 1
    return result

def formingMagicSquare(s):
    result = []
    corners = [ [8, 4, 6, 2],
                [2, 4, 6, 8],
                [8, 6, 4, 2],
                [2, 6, 4, 8],
                [4, 2, 8, 6],
                [6, 2, 8, 4],
                [4, 8, 2, 6],
                [6, 8, 2, 4] ]
    for c in corners:
        total_cost = 0
        total_cost += abs(s[0][0] - c[0])
        total_cost += abs(s[0][2] - c[1])
        total_cost += abs(s[2][0] - c[2])
        total_cost += abs(s[2][2] - c[3])
        total_cost += abs(s[1][1] - 5)
        total_cost += abs(s[0][1] - (15 - c[0] - c[1]))
        total_cost += abs(s[1][0] - (15 - c[0] - c[2]))
        total_cost += abs(s[1][2] - (15 - c[1] - c[3]))
        total_cost += abs(s[2][1] - (15 - c[2] - c[3]))
        result.append(total_cost)
    return min(result)

#Easy
def count_zigzag(numbers):
    result = []
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] and numbers[i + 1] < numbers[i]:
            result.append(1)
        elif numbers[i - 1] > numbers[i] and numbers[i + 1] > numbers[i]:
            result.append(1)
        else:
            result.append(0)
    return result

def arrays_concatenation(a, b, k):
    result = 0
    for i in range(len(a)):
        num_a = str(a[i])
        num_b = str(b[len(b) - i - 1])
        concat = int(num_a + num_b)
        if concat < k:
            result += 1
    return result


#Optimized solutions
def climbingLeaderboard(ranked, player):
    result = []
    player.sort(reverse=True)
    cur_rank = 1
    cur_pos = 0
    prev = ranked[0]
    while player != []:
        if cur_pos == len(ranked):
            result.append(cur_rank + 1)
            player.pop(0)
        else:
            if prev != ranked[cur_pos]:
                cur_rank += 1
                prev = ranked[cur_pos]
            if player[0] >= ranked[cur_pos]:
                result.append(cur_rank)
                player.pop(0)
            else:
                cur_pos += 1
    result.sort(reverse=True)
    return result

def saveThePrisoner(n, m, s):
    m = m % n
    ans = s + m - 1
    if ans == n:
        return n
    elif ans > n:
        return ans - n
    else:
        return s + m - 1 
    
a = saveThePrisoner(6, 737005495, 6)
print(a)

def queensAttack(n, k, r_q, c_q, obstacles):
    ob_dict = {'left': [], 'right': [], 'up': [], 'down': [],
    'leftup': [], 'leftdown': [], 'rightup': [], 'rightdown': []}
    for ob in obstacles:
        if ob[0] == r_q and ob[1] < c_q :
            ob_dict['left'].append(abs(ob[1] - c_q))
        elif ob[0] == r_q and ob[1] > c_q:
            ob_dict['right'].append(ob[1] - c_q)
        elif ob[1] == c_q and ob[0] > r_q:
            ob_dict['up'].append(ob[0] - r_q)
        elif ob[1] == c_q and ob[0] < r_q:
            ob_dict['down'].append(abs(ob[0] - r_q))
        elif abs(r_q - ob[0]) == abs(c_q - ob[1]):
            r_diff = ob[0] - r_q
            c_diff = ob[1] - c_q
            if r_diff >= 1 and c_diff <= -1:
                ob_dict['leftup'].append(ob[0] - r_q)
            elif r_diff >= 1 and c_diff >= 1:
                ob_dict['rightup'].append(ob[0] - r_q)
            elif r_diff <= -1 and c_diff <= -1:
                ob_dict['leftdown'].append(abs(ob[1] - c_q))
            elif r_diff <= -1 and c_diff >= 1:
                ob_dict['rightdown'].append(abs(ob[1] - c_q))
    count = 0
    for key in ob_dict:
        if ob_dict[key] != []:
            count += (min(ob_dict[key]) - 1)
        else:
            if key == 'left':
                count += (c_q - 1)
            elif key == 'right':
                count += (n - c_q)
            elif key == 'up':
                count += (n - r_q)
            elif key == 'down':
                count += (r_q - 1)
            elif key == 'leftup':
                count += min(c_q - 1, n - r_q)
            elif key == 'rightup':
                count += min(n - c_q, n - r_q)
            elif key == 'leftdown':
                count += min(c_q - 1, r_q - 1)
            elif key == 'rightdown':
                count += min(n - c_q, r_q - 1)
    return count

def encryption(s):
    msg = []
    row = math.floor(len(s) ** 0.5)
    col = math.ceil(len(s) ** 0.5)
    for j in range(row + 1):
        msg.append('')
    for i in range(len(s)):
        msg[i % col] += s[i]
    enc_msg = ' '.join(msg)
    return enc_msg

def biggerIsGreater(w):
    if len(w) == 2 and w[0] != w[1]:
        return w[1] + w[0]
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    i -= 1
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    print(i, j, w[i], w[j])
    tmp = w[i+1:j] + w[i] + w[j+1:]
    tmp = tmp[::-1]
    return w[:i] + w[j] + tmp

print(biggerIsGreater('0125664'))