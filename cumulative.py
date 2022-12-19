import sys

#1.
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] + nums[i]

for _ in range(m):
    x, y = map(int, input().split())
    print(dp[y] - dp[x-1])

#timeover
# n, m = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))
# for _ in range(m):
#     start, end = map(int, sys.stdin.readline().split())
#     length = 0
#     while start <= end:
#         length += nums[start-1]
#         start += 1
#
#     print(length)


#2.
n, k = map(int, input().split())
temp = list(map(int, input().split()))

part_sum = sum(temp[:k])
result = [part_sum]

for i in range(n-k):
    part_sum = part_sum - temp[i] + temp[i+k]
    result.append(part_sum)

print(max(result))

#timeover
# input = sys.stdin.readline
# n, k = map(int, input().split())
# temp = list(map(int, input().split()))
#
# dp = [0] * (n-k+2)
# for i in range(n-k+1):
#     dp[i+1] = sum(temp[i: k+i])
#
# print(max(dp))


#3.
#50점,,?
# word = input()
# t = int(input())
# for i in range(t):
#     alphabet, start, end = input().split()
#     start, end = int(start), int(end)
#     print(word[start: end+1].count(alphabet))

#100점
input = sys.stdin.readline

word = input().rstrip()
arr = [[0]*26]
arr[0][ord(word[0])-97] = 1
for i in range(1, len(word)):
    arr.append(arr[-1][:])
    arr[i][ord(word[i])-97] += 1

for _ in range(int(input())):
    c, start, end = list(input().split())
    start, end = map(int, [start, end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])


#4.
n, m = map(int, input().split())
nums = list(map(int, input().split()))

prepix = [0 for i in range(m)]
presum = 0
prepix[0] = 1

for i in range(n):
    presum += nums[i]
    prepix[presum % m] += 1

cnt = 0
for i in prepix:
    cnt += i*(i-1)//2
print(cnt)

#memory over
# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# cnt = 0
#
# for k in range(2, n+1):
#     dp = [0] * (n-k+2)
#     for i in range(n-k+1):
#         dp[i+1] = sum(nums[i:i+k])
#         nums.append(dp[i+1])
#
# print(nums)
# for num in nums:
#     if num % m == 0:
#         cnt += 1
#
# print(cnt)


#5.
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + nums[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

#timeover
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(m):
#     total = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             total += board[i][j]
#     print(total)


#6.
def chess(color):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + value

    count = int(1e9)
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, dp[i+k-1][j+k-1] - dp[i+k-1][j-1] - dp[i-1][j+k-1] + dp[i-1][j-1])
    return count


input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
print(min(chess('W'), chess('B')))


#another solution
# def main():
#     # pylint: disable=unused-variable
#     N, M, K = [int(x) for x in sys.stdin.readline().split()]
#     board = [sys.stdin.readline().rstrip() for _ in range(N)]
#
#     dp = [[0] * (M + 1)]
#     for row, psum_row_prev, target in zip(board, dp, 'BW' * N):
#         psum_row_cur = [0]
#         rsum = 0
#         for ch, ps in zip(row, dp[1:]):
#             rsum += ch == target
#             target = 'B' if target == 'W' else 'W'
#             psum_row_cur.append(ps + rsum)
#         dp.append(psum_row_cur)
#
#     answer = K * K
#     for beg, end in zip(dp, dp[K:]):
#         for bb, be, eb, ee in zip(beg, beg[K:], end, end[K:]):
#             s = ee - be - eb + bb
#             answer = min(answer, s, K * K - s)
#
#     print(answer)
#
#
# if __name__ == '__main__':
#     main()
