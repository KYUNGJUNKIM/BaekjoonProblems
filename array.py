#1 공넣기(10810)
# n, m = map(int, input().split())
#
# balls = [[0] for i in range(n+1)]
#
# for _ in range(m):
#     i, j, k = map(int, input().split())
#     for idx in range(i, j+1):
#         balls[idx].append(k)
#
# for x in range(1, len(balls)):
#     print(balls[x][-1], end=' ')


#2 공바꾸기(10813)
# n, m = map(int, input().split())
# nums = [i for i in range(n+1)]
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     x, y = nums[i], nums[j]
#     nums[i], nums[j] = y, x
#
# for x in range(1, len(nums)):
#     print(nums[x], end=' ')


#3 바구니뒤집기(10811)
# n, m = map(int, input().split())
# nums = [i for i in range(n+1)]
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     temp = nums[i:j+1]
#     nums[i:j+1] = temp[::-1]
# for x in range(1, len(nums)):
#     print(nums[x], end=' ')


#4. 세로읽기(10798)

# words = [[0] * 15 for i in range(5)]
#
# for i in range(5):
#     d = list(input())
#     for j in range(len(d)):
#         words[i][j] = d[j]
#
# for i in range(15):
#     for j in range(5):
#         if words[j][i] == 0:
#             continue
#         else:
#             print(words[j][i], end='')
