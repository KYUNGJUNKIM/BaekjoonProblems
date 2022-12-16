import sys

#1.
print(ord(input()))


#2.
n = int(input())
num = sys.stdin.readline().rstrip()
total = 0
for i in range(len(num)):
    total += int(num[i])
print(total)


#3.
# word = sys.stdin.readline().rstrip()
# alphabet = [chr(i) for i in range(97, 123)]
#
# for x in range(len(alphabet)):
#     for idx in range(len(word)):
#         if alphabet[x] == word[idx]:
#             if type(alphabet[x]) == str:
#                 alphabet[x] = idx
#
# for x in range(len(alphabet)):
#     if type(alphabet[x]) != int:
#         alphabet[x] = -1
#     print(alphabet[x], end=' ')


#another solution with find function
S = input()
arr = list(range(97, 123))

for i in arr:
    print(S.find(chr(i)), end=' ')


#4.
t = int(input())
for i in range(t):
    ans = ''
    times, string = sys.stdin.readline().rstrip().split()
    for idx in range(len(string)):
        ans += string[idx] * int(times)
    print(ans)


#5.
from collections import Counter
s = sys.stdin.readline().upper().rstrip()
letter = [s[x] for x in range(len(s))]
check = list(set(letter))
if len(check) >= 2:
    common = Counter(letter).most_common(2)

    if common[0][1] == common[1][1]:
        print('?')
    else:
        print(common[0][0])

elif len(check) == 1:
    print(check[0])

else:
    print('?')


#6.
sentence = sys.stdin.readline().rstrip()
words = sentence.split()
print(len(words))


#7.
x, y = sys.stdin.readline().rstrip().split()
x1, y1 = '', ''
for i in range(len(x)-1, -1, -1):
    x1 += x[i]
for j in range(len(y)-1, -1, -1):
    y1 += y[j]

if int(x1) > int(y1):
    print(x1)
else:
    print(int(y1))


#8.
dial = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
s = input()
letters = list(s[i] for i in range(len(s)))
total = 0
for x in range(len(dial)):
    for y in dial[x]:
        for z in range(len(letters)):
            if letters[z] in y:
                total += x + 2

print(total)

# better solution
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)


#9.
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().rstrip()
cnt = 0
for alphabet in alphabets:
    if alphabet in s:
        s = s.replace(alphabet, '!')

print(len(s))


#10.
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)








