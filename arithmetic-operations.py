#1.
n = int(input())
result = 0
for i in range(1, n+1):
    result += i
print(result)

#2.
X = int(input())
N = int(input())
result = 0
for _ in range(N):
    a, b = map(int, input().split())
    result += a*b

if X == result:
    print("Yes")
else:
    print("No")

#3.
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

# 4.
n = int(input())
for i in range(1, n+1):
    print((' ' * (n-i)) + ('*' * i))

#5.
n = int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt = cnt+1
    if num == n:
        print(cnt)
        break


