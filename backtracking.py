import sys
import itertools

#1.
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

for item in list(itertools.permutations(num, m)):
    for i in range(m):
        print(item[i], end=' ')
    print()


#2.
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

for item in list(itertools.combinations(num, m)):
    for i in range(m):
        print(item[i], end=' ')
    print()

#combination function
def n_length_combo(arr, n):
    if n == 0:
        return [[]]

    lst = []
    for i in range(len(arr)):
        m = arr[i]
        remArr = arr[i+1:]

        remArr_combo = n_length_combo(remArr, n - 1)
        for j in remArr_combo:
            lst.append([m, *j])
    return lst


def n_length_combo_with_replacement(arr, n):
    if n == 0:
        return [[]]

    lst = []
    for i in range(len(arr)):
        m = arr[i]
        remArr = arr[i:]

        remArr_combo = n_length_combo_with_replacement(remArr, n-1)
        for j in remArr_combo:
            lst.append([m, *j])
    return lst


#3.
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

for item in list(itertools.product(num, repeat=m)):
    for j in range(m):
        print(item[j], end=' ')
    print()


#4.
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

for item in list(itertools.combinations_with_replacement(num, m)):
    for j in range(m):
        print(item[j], end=' ')
    print()

print(n_length_combo_with_replacement(num, m))


#6. sudoku
def check(x, y):
    nums = [i for i in range(1, 10)]

    for p in range(9):
        if board[x][p] in nums:
            nums.remove(board[x][p])
        if board[p][y] in nums:
            nums.remove(board[p][y])

    x = x // 3 * 3
    y = y // 3 * 3

    for p in range(x, x+3):
        for q in range(y, y+3):
            if board[p][q] in nums:
                nums.remove(board[p][q])

    return nums


def dfs(x):
    if x == len(zero_cord):
        for row in board:
            print(*row)
        return

    else:
        i, j = zero_cord[x][0], zero_cord[x][1]
        num_to_check = check(i, j)

        for num in num_to_check:
            board[i][j] = num
            dfs(x+1)
            board[i][j] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero_cord = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
dfs(0)


#7.
import itertools
import math
t = int(input())
nums = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

if sum(operator_num) == 1:
    total = 0
    if operator_num.index(1) == 0:
        total = nums[0] + nums[1]
    elif operator_num.index(1) == 1:
        total = nums[0] - nums[1]
    elif operator_num.index(1) == 2:
        total = nums[0] * nums[1]
    elif operator_num.index(1) == 3:
        total = nums[0] // nums[1]
    print(total)
    print(total)

else:
    operator = []
    for i in range(len(operator_num)):
        for j in range(operator_num[i]):
            if i == 0:
                operator.append('+')
            elif i == 1:
                operator.append('-')
            elif i == 2:
                operator.append('*')
            elif i == 3:
                operator.append('/')

    operator_list = list(itertools.permutations(operator, len(operator)))
    operator_list = list(set(operator_list))

    result = []
    for equation in operator_list:
        total = nums[0]
        for x in range(len(equation)):
            if equation[x] == '+':
                total += nums[x+1]
            elif equation[x] == '-':
                total -= nums[x+1]
            elif equation[x] == '*':
                total *= nums[x+1]
            elif equation[x] == '/':
                if total < 0:
                    total = math.trunc(total / nums[x+1])
                else:
                    total //= nums[x+1]
        result.append(total)

    print(max(result))
    print(min(result))


#using dfs
# n = int(input())
# nums = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
#
# maximum = -1e9
# minimum = 1e9
#
#
# def dfs(depth, total, add, sub, mul, div):
#     global maximum, minimum
#     if depth == n:
#         maximum = max(maximum, total)
#         minimum = min(minimum, total)
#
#     if add > 0:
#         dfs(depth+1, total+nums[depth], add-1, sub, mul, div)
#     if sub > 0:
#         dfs(depth+1, total-nums[depth], add, sub-1, mul, div)
#     if mul > 0:
#         dfs(depth+1, total*nums[depth], add, sub, mul-1, div)
#     if div > 0:
#         dfs(depth+1, int(total/nums[depth]), add, sub, mul, div-1)
#
#
# dfs(1, nums[0], add, sub, mul, div)
# print(maximum)
# print(minimum)


#8.
def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += board[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return


    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, idx+1)
            visited[i] = False


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)


