import sys

#1.
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cards.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(cards, nums[i], 0, n - 1) is None:
        print(0, end=' ')
    else:
        print(1, end=' ')

#시간 초과
# n = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
#
# results = []
# for num in nums:
#     if num in cards:
#         results.append(1)
#     else:
#         results.append(0)
#
# for result in results:
#     print(result, end=' ')


#2.
n, m = map(int, sys.stdin.readline().split())
words = set()
for _ in range(n):
    words.add(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(m):
    test = sys.stdin.readline().rstrip()
    if test in words:
        cnt += 1
print(cnt)


#3.
n, m = map(int, sys.stdin.readline().split())

pokemon_int_key = {}
pokemon_name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokemon_int_key[i] = name
    pokemon_name_key[name] = i

for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit():  # isdigit -> O(n)
        print(pokemon_int_key[int(item)-1])
    else:
        print(pokemon_name_key[item]+1)


#시간 초과
# n, m = map(int, sys.stdin.readline().split())
# num = [str(i) for i in range(1, n+1)]
# pokemons = []
# for i in range(n):
#     pokemon = {'order': str(i), 'name': sys.stdin.readline().rstrip()}
#     pokemons.append(pokemon)
#
# for _ in range(m):
#     test = sys.stdin.readline().rstrip()
#     for pokemon in pokemons:
#         if test == pokemon['order']:
#             print(pokemon['name'])
#         if test == pokemon['name']:
#             print(int(pokemon['order'])+1)
#


#4.
from collections import Counter
n = int(sys.stdin.readline())
cards = sys.stdin.readline().split()
m = int(sys.stdin.readline())
tests = sys.stdin.readline().split()

cnts = Counter(cards)
print(' '.join(f'{cnts[test]}' if test in cnts else '0' for test in tests))


#시간 초과
# n = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# tests = list(map(int, sys.stdin.readline().split()))
#
# cnts = []
# for test in tests:
#     cnt = 0
#     for card in cards:
#         if test == card:
#             cnt += 1
#     cnts.append(cnt)
#
# for cnt in cnts:
#     print(cnt, end=' ')


#5.
n, m = map(int, input().split())

unknown = set()
for _ in range(n):
    unknown.add(sys.stdin.readline().rstrip())
known = set()
for _ in range(m):
    known.add(sys.stdin.readline().rstrip())

ppl = sorted(list(unknown & known))
print(len(ppl))
for person in ppl:
    print(person)

#시간 초과
# n, m = map(int, input().split())
#
# unknown = []
# for _ in range(n):
#     ppl = sys.stdin.readline().rstrip()
#     unknown.append(ppl)
#
# known = []
# cnt = 0
# for _ in range(m):
#     name = sys.stdin.readline().rstrip()
#     if name in unknown:
#         known.append(name)
#         cnt += 1
#
# print(cnt)
# for person in known:
#     print(person)


#6.
n, m = map(int, input().split())

list1 = list(map(int, sys.stdin.readline().split()))
set1 = set(list1)
list2 = list(map(int, sys.stdin.readline().split()))
set2 = set(list2)

diff1 = set1 - set2
diff2 = set2 - set1

print(len(diff1) + len(diff2))


#7.
s = sys.stdin.readline().rstrip()
subset = []
for i in range(len(s)):
    subset.append(s[i])
    for j in range(i+1, len(s)):
        subset.append(s[i:j+1])
subset = sorted(set(subset))
subset.sort(key=len)
print(len(subset))





