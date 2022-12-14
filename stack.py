import sys

#1.
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.append(word[1])
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)


#2.
k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))


#3.
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    total = 0
    string = sys.stdin.readline().rstrip()
    for i in range(len(string)):
        if string[i] == '(':
            total += 1
        elif string[i] == ')':
            total -= 1
        if total < 0:
            print("NO")
            break
    if total > 0:
        print("NO")
    elif total == 0:
        print("YES")


#4.
while True:
    arr = sys.stdin.readline().rstrip()
    stack = []

    if arr == ".":
        break

    for i in arr:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


#5.
n = int(input())
stack, answer = [], []
flag, cur = 0, 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for ans in answer:
        print(ans)





