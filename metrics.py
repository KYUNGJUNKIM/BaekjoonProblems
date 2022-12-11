#1.
N, M = map(int, input().split())
list1 = [list(map(int, input().split())) for _ in range(N)]
list2 = [list(map(int, input().split())) for _ in range(N)]
for row in range(N):
    for col in range(M):
        print(list1[row][col] + list2[row][col], end=' ')
    print()

#2.
x, y = 0, 0
maximum = -1

for i in range(9):
    board = list(map(int, input().split()))
    for j in range(9):
        if board[j] > maximum:
            maximum = board[j]
            x, y = i+1, j+1

print(maximum)
print(x, y)

#3.
n = int(input())
paper = [[0]*101 for i in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

width = 0
for items in paper:
    for item in items:
        if item == 1:
            width += 1
print(width)

#sol2
# for i in paper:
#     width += sum(i)
# print(width)


# 겹치는 부분의 넓이를 구하고 싶을 때
# for _ in range(n):
#     a, b = map(int, input().split())
#     for i in range(10):
#         for j in range(10):
#             paper[a+i][b+j] += 1
#
# r = 0
# for i in range(101):
#     for j in paper[i]:
#         if j >= 2:
#             r += 1
# print(r)

