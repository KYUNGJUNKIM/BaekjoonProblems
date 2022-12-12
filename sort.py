import sys

#1.
n = int(input())
result = []
for i in range(n):
    num = int(input())
    result.append(num)
result = sorted(result)
for item in result:
    print(item)

# without sorted
def bubbleSort(x):
    for i in range(len(x) - 1):
        for j in range((len(x) - 1) - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

def quickSort(x):
    if len(x) <= 1:
        return x
    pivot = x[len(x)//2]
    left, right, equal = [], [], []
    for a in x:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)
    return quickSort(left) + equal + quickSort(right)


#2.
n = int(input())
nums = []
for i in range(n):
    n = int(input())
    nums.append(n)
nums = sorted(nums)
total = 0
for num in nums:
    total += num
avg = total / 5
if len(nums) % 2 == 0:
    median = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
else:
    median = nums[(n-1)//2]
print(avg)
print(median)


#3.
n, k = map(int, input().split())
score = list(map(int, input().split()))
score = sorted(score)
print(score[-k])


# 4.
n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for i in num:
    print(i)


#5.
n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)


#6.
from collections import Counter

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

avg = round(sum(num)/n)
print(avg)
median = (num[(n-1)//2])
print(median)

nums_s = Counter(num).most_common()
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

variation = max(num) - min(num)
print(variation)


#7.
n = input()
nums = [int(x) for x in n]
nums.sort(reverse=True)
result = ''
for num in nums:
    result += str(num)
print(result)


#8.
# n = int(input())
# cps = []
# for i in range(n):
#     cp = list(map(int, input().split()))
#     cps.append(cp)
# for i in range((len(cps)-1)):
#     for j in range(len(cps)-1-i):
#         if cps[j][0] > cps[j+1][0]:  # x 좌표가 클 때
#             cps[j], cps[j+1] = cps[j+1], cps[j]
#         elif cps[j][0] == cps[j+1][0]:  # x 좌표가 동일할 때
#             if cps[j][1] > cps[j+1][1]:  # y 좌표 비교
#                 cps[j], cps[j+1] = cps[j+1], cps[j]
#
# for i in range(len(cps)):
#     print(cps[i][0], cps[i][1])

#-- solution
n = int(sys.stdin.readline())
num = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x, y])
num.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(num[i][0], num[i][1])


#9.
n = int(sys.stdin.readline())

cps = []
for _ in range(n):
    cp = list(map(int, sys.stdin.readline().split()))
    cps.append(cp)
cps.sort(key= lambda x: (x[1], x[0]))

for i in range(len(cps)):
    print(cps[i][0], cps[i][1])

#10.
n = int(sys.stdin.readline())
words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())
words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
    print(word)

# 시간 초과....
# n = int(sys.stdin.readline())
# words = []
# words_without = []
# for _ in range(n):
#     word = sys.stdin.readline()
#     words.append({'word': word.rstrip(), 'length': len(word)-1})
#
# for word in words:
#     if word not in words_without:
#         words_without.append(word)
#
# words_without.sort(key=lambda x: (x['length'], x['word']))
#
# for word in words_without:
#     print(word['word'])

#11.
n = int(sys.stdin.readline())
info = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    info.append([int(age), name])
info.sort(key=lambda x: x[0])

for x in info:
    print(x[0], x[1])

#12.
n = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
num2 = list(sorted(set(num1)))

dic = {num2[i]: i for i in range(len(num2))}

for i in num1:
  print(dic[i], end=' ')


# 시간 초과....
# n = int(sys.stdin.readline())
#
# num = list(map(int, sys.stdin.readline().split()))
# count = [0] * len(num)
# for i in range(len(num)):
#     for j in range(len(num)):
#         if i != j:
#             if num[i] > num[j]:
#                 count[i] += 1
# print(count)


