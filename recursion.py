import sys

#1.
n = int(sys.stdin.readline())
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(n))


#2.
n = int(sys.stdin.readline())
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(n))


#3.
def recursion(char, left, right):
    global cnt
    cnt += 1

    if left >= right:
        return 1
    elif char[left] != char[right]:
        return 0
    else:
        return recursion(char, left+1, right-1)

def isPalindrome(char):
    return recursion(char, 0, len(char)-1)


n = int(sys.stdin.readline())
words = list(sys.stdin.readline().rstrip() for i in range(n))
for word in words:
    cnt = 0
    print(isPalindrome(word), cnt)


#4.
def merge_sort(A, p, r):
    if p < r and count <= k:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global count, result
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i, t = p, 0

    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == k:
            result = A[i]
            break
        i += 1
        t += 1


n, k = map(int, input().split())
num = list(map(int, input().split()))
count = 0
result = -1
merge_sort(num, 0, n-1)
print(result)

#5.
def draw_stars(n):
    if n == 1:
        return ['*']

    stars = draw_stars(n//3)
    arr = []

    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star + ' '*(n//3) + star)
    for star in stars:
        arr.append(star*3)

    return arr


k = int(sys.stdin.readline())
print('\n'.join(draw_stars(k)))

#6.
def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)  # 1step
    print(start, end)  # 2step
    hanoi_tower(n - 1, 6 - start - end, end)  # 3step


k = int(sys.stdin.readline())
print(2 ** k - 1)
hanoi_tower(k, 1, 3)



