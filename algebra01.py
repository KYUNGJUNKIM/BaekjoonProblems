import sys

#1.
import math
fixed_cost, production_cost, price = map(int, sys.stdin.readline().split())

if production_cost >= price:
    print(-1)
else:
    print(math.trunc(fixed_cost/(price - production_cost)) + 1)


#2.
n = int(input())
i = 0
while True:
    if n <= (3*i*(i+1) + 1):
        print(i+1)
        break
    i += 1


#3.
n = int(input())

line, end = 0, 0
while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0:
    numerator = line - diff
    denominator = diff + 1
else:
    numerator = diff + 1
    denominator = line - diff

print(f"{numerator}/{denominator}")


#4.
import math
a, b, v = map(int, input().split())
print(math.ceil((v-a)/(a-b)) + 1)


#5.
n = int(input())
for i in range(2):
    h, w, order = map(int, input().split())
    floor = order % h
    num = (order // h) + 1
    if order % h == 0:
        floor = h
        num = order // h
    print(f'{floor * 100 + num}')


#6.
t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    floor0 = [x for x in range(1, num+1)]
    for i in range(floor):
        for j in range(1, num):
            floor0[j] += floor0[j-1]
    print(floor0[-1])


#7.
num = int(input())
cnt = 0

while num >= 0:
    if num % 5 == 0:
        cnt += num // 5
        print(cnt)
        break

    num -= 3
    cnt += 1

else:
    print(-1)


#8.
a, b = map(int, sys.stdin.readline().split())
print(a+b)

