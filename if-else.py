import sys

#1.
x, y = map(int, input().split())
if x > y:
    print('>')
elif x == y:
    print('==')
else:
    print('<')


#2.
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')


#3.
n = int(input())
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)


#4.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)


#5.
h, m = map(int, input().split())
if m < 45:
    if h == 0:
        h = 23
    else:
        h -= 1
    m += 15
else:
    m -= 45
print(h, m)


#6.
H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)


#7.
a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000 + a*1000)

if a == b and b != c:
    print(1000 + a*100)
elif a == c and b != c:
    print(1000 + a*100)
elif b == c and a != c:
    print(1000 + b*100)

if a != b and b != c and c != a:
    print(max([a, b, c])*100)







