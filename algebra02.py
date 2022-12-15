import sys

#1.
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

prime = 0
for num in nums:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            prime += 1
print(prime)


#2.
m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))


#3.
N = int(input())
denominator = 2
while N != 1:
    if N % denominator == 0:
        print(denominator)
        N = N // denominator
    else:
        denominator += 1


#4.
m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)

#time over
# x, y = map(int, input().split())
# while x < y:
#     for i in range(2, x+1):
#         if x % i == 0:
#             break
#     else:
#         print(x)
#     x += 1


#5.
def check_prime(a, b):
    cnt = 0
    arr = [True] * (b + 1)

    for i in range(2, int(b**0.5 + 1)):
        if arr[i]:
            for j in range(i*2, b+1, i):
                arr[j] = False

    for k in range(a+1, b+1):
        if arr[k]:
            cnt += 1
    return cnt


while True:
    n = int(input())
    if n == 0:
        break
    print(check_prime(n, 2*n))


#time over
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0
#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             continue
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 break
#         else:
#             cnt += 1
#     print(cnt)


#6.
def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1

#time over
# t = int(input())
# for i in range(t):
#     n = int(input())
#
#     if n % 2 != 0:
#         continue
#
#     else:
#         result = []
#         for x in range(2, n):
#             for y in range(2, int(x ** 0.5) + 1):
#                 if x % y == 0:
#                     break
#             else:
#                 result.append(x)
#
#     result2 = []
#     for item in result:
#         if n - item in result and item <= n-item:
#             result2.append([item, n-item])
#     result2.sort(key=lambda x:(abs(x[0]-x[1])))
#     print(result2[0][0], result2[0][1])













