import sys

#1.
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0

for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            if cards[x] + cards[y]+ cards[z] > m:
                continue
            else:
                result = max(result, cards[x]+cards[y]+cards[z])
print(result)

# 시간 초과....
# n, m = map(int, sys.stdin.readline().split())
# cards = list(map(int, sys.stdin.readline().split()))
#
#
# results = []
# for x in range(len(cards)):
#     for y in range(x+1, (len(cards))):
#         for z in range(y+1, len(cards)):
#             results.append(cards[x] + cards[y] + cards[z])
#
# results = list(set(results))
# results.sort()
#
# for i in range(len(results)):
#     if results[i] == m:
#         print(results[i])
#         break
#     if results[i] > m:
#         print(results[i-1])
#         break


#2.
n = int(sys.stdin.readline())
result = 0
for i in range(1, n+1):
    arr = list(map(int, str(i)))
    result = i + sum(arr)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)  # 생성자 없음


#3.
n = int(sys.stdin.readline())

ppl = []
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    ppl.append([weight, height])

rank = []
for x in range(len(ppl)):
    cnt = 0
    for y in range(len(ppl)):
        if ppl[x][0] < ppl[y][0] and ppl[x][1] < ppl[y][1]:
            cnt += 1
    rank.append(cnt+1)

for ranking in rank:
    print(ranking, end=' ')


#4.
n, m = map(int, sys.stdin.readline().split())
board = []
result = []

for _ in range(n):
    board.append(sys.stdin.readline())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
                else:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))


#5.
n = int(sys.stdin.readline())

num666 = []
for i in range(666, 3000000):  # while 문을 써도 무방
    if '666' in str(i):
        num666.append(i)
num666.sort()

print(num666[n-1])






