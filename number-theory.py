import sys

#1.
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if y % x == 0:
        print('factor')
    elif x % y == 0:
        print('multiple')
    else:
        print('neither')


#2.
n = int(input())
measure = list(map(int, input().split()))
measure.sort()
print(measure[0] * measure[-1])


#3.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


x, y = map(int, input().split())
print(gcd(x, y))
print(lcm(x, y))

def gcd_for(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


#4.
def gcb(x, y):
    while y > 0:
        temp = x % y
        x = y
        y = temp
    return x


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lcm = a * b // gcb(a, b)
    print(lcm)



#5.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
num = sorted([int(input()) for _ in range(n)])
re_num = []

for i in range(1, n):
    re_num.append(num[i] - num[i-1])

GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = gcd(GCD, re_num[idx])

result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))

#time over
# n = int(input())
# nums = [int(input()) for _ in range(n)]
#
# for i in range(2, min(nums)+1):
#     result = set()
#     for num in nums:
#         result.add(num % i)
#     if len(set(result)) == 1:
#         print(i, end=' ')


#6.
def gcb(a, b):
    if b == 0:
        return a
    else:
        return gcb(b, a % b)


def lcm(a, b):
    return a*b // gcb(a, b)


n = int(input())
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    if nums[0] % nums[i] == 0:
        print(f'{int(nums[0]/nums[i])}/1')
    else:
        print(f'{int(lcm(nums[0], nums[i])/nums[i])}/{int(lcm(nums[0], nums[i])/nums[0])}')


#7.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


n, c = map(int, input().split())
print(factorial(n) // (factorial(c) * factorial(n-c)))


#8.
# from math import factorial
# n, k = map(int, input().split())
# result = factorial(n) // (factorial(k) * factorial(n - k))
# print(result % 10007)


#without factorial
#https://pacific-ocean.tistory.com/207
n, k = map(int, input().split())
dp = [[0] for _ in range(1001)]
dp[1].append(1)
for i in range(2, 1001):
    for j in range(1, i+1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
print(dp[n+1][k+1] % 10007)

#9.
from math import factorial
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))


#10.
from collections import Counter
t = int(input())
for i in range(t):
    wear = [sys.stdin.readline().rstrip().split() for _ in range(int(input()))]
    wear_cat = [wear[i][1] for i in range(len(wear))]
    counter = Counter(wear_cat).most_common(len(wear_cat))

    num_cat = 1
    for j in range(len(counter)):
        num_cat *= (counter[j][1] + 1)

    print(num_cat-1)


#11.
n = int(input())
cnt = 0
while n != 0:
    n = n // 5
    cnt += n
print(cnt)


#another solution
# N = int(input())
# print(N//5 + N//25 + N//125)


#12.
def count2(x):
    two = 0
    while x != 0:
        x = x // 2
        two += x
    return two


def count5(x):
    five = 0
    while x != 0:
        x = x // 5
        five += x
    return five


n, m = map(int, input().split())
print(min(count2(n)-count2(m)-count2(n-m), count5(n)-count5(m)-count5(n-m)))


# time over or memory error
# from math import factorial
# n, m = map(int, input().split())
# cnt = 0
#
# result = str(factorial(n) // (factorial(m) * factorial(n-m)))
# for i in range(len(result)-1, -1, -1):
#     if result[i] == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)


