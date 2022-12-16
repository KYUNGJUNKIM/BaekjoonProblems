import sys

#1.
n = int(input())
arr = list(map(int, input().split()))
v = int(input())
print(arr.count(v))


#2.
n, x = map(int, input().split())
arr = list(map(int, input().split()))

for num in arr:
    if num < x:
        print(num, end=' ')


#3.
n = int(input())
arr = list(map(int, input().split()))

print(min(arr), max(arr))


#4.
arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

maximum, idx = 0, 0
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
        idx = i+1

print(maximum)
print(idx)


#5.
attendance = []
for _ in range(28):
    n = int(input())
    attendance.append(n)
attendance.sort()
for i in range(1, 31):
    if i not in attendance:
        print(i)


#6.
nums = []
for _ in range(10):
    n = int(input())
    nums.append(n)

for i in range(len(nums)):
    nums[i] = nums[i] % 42
print(len(set(nums)))


#7.
n = int(input())
scores = list(map(int, input().split()))

maximum = max(scores)
for i in range(len(scores)):
    scores[i] = (scores[i] / maximum) * 100
print(sum(scores)/len(scores))


#8.
t = int(input())
for i in range(t):
    score = 0
    ans = sys.stdin.readline().rstrip()
    ans = ans.split('X')
    for item in ans:
        for j in range(1, len(item)+1):
            score += j
    print(score)


#9.
t = int(input())
for i in range(t):
    scores = list(map(int, input().split()))
    cnt = 0
    for j in range(1, len(scores)):
        avg = sum(scores[1:]) / scores[0]
        if scores[j] > avg:
            cnt += 1
    print(f'{cnt/scores[0]*100:.3f}%')

