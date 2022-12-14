import sys

#1.
x, y, w, h = map(int, input().split())
distance = [x, y, w - x, h - y]

print(min(distance))


#2.
cord = []
for _ in range(3):
    x, y = map(int, input().split())
    cord.append([x, y])

new_x, new_y = 0, 0
if cord[0][0] == cord[1][0]:
    new_x = cord[2][0]
elif cord[1][0] == cord[2][0]:
    new_x = cord[0][0]
else:
    new_x = cord[1][0]

if cord[0][1] == cord[1][1]:
    new_y = cord[2][1]
elif cord[1][1] == cord[2][1]:
    new_y = cord[0][1]
else:
    new_y = cord[1][1]

print(new_x, new_y)


#3.
# import math
# while True:
#     x, y, z = map(int, input().split())
#     if x == 0 and y == 0 and z == 0:
#         break
#
#     if x == max(x, y, z) and y+z > x:
#         if math.sqrt(y**2 + z**2) == x:
#             print('right')
#         else:
#             print('wrong')
#     if y == max(x, y, z) and x+z > y:
#         if math.sqrt(x**2 + z**2) == y:
#             print('right')
#         else:
#             print('wrong')
#     if z == max(x, y, z) and x+y > z:
#         if math.sqrt(x**2 + y**2) == z:
#             print('right')
#         else:
#             print('wrong')

# Classic Solution
while True:
    nums = list(map(int, input().split()))
    max_num = max(nums)
    if sum(nums) == 0:
        break

    nums.remove(max_num)
    if nums[0] ** 2 + nums[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')


#4.
n = int(input())
board = [list(map(int, input().split())) for _ in range(6)]

maximum_width, max_windex, maximum_height, max_hindex = 0, 0, 0, 0
for i in range(6):
    if board[i][0] == 1 or board[i][0] == 2:
        if board[i][1] > maximum_width:
            maximum_width = board[i][1]
            max_windex = i

    elif board[i][0] == 3 or board[i][0] == 4:
        if board[i][1] > maximum_height:
            maximum_height = board[i][1]
            max_hindex = i

minimum_height = abs(board[max_windex+1][1] - board[max_windex-1][1])
minimum_width = abs(board[max_hindex+1][1] - board[max_hindex-1][1])

print(n * ((maximum_height * maximum_width) - (minimum_height * minimum_width)))


#5.
import math
n = int(input())

euclidean = (n ** 2) * math.pi
taxi = (2 * n) * n

print(euclidean)
print(taxi)





