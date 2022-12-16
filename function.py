#1.
def solve(n):
    ans = 0
    for num in n:
        ans += num
    return ans


#2.
def self_number():
    nums = [i for i in range(1, 10001)]
    dn = []

    for num in nums:
        if num < 10:
            a = num * 2
            if a in nums:
                dn.append(a)
        else:
            total = 0
            for j in range(len(str(num))):
                total += int(str(num)[j])
            a = num + total
            if a in nums:
                dn.append(a)

    dn = set(dn)
    return dn


ans = set([i for i in range(1, 10001)]) - self_number()
for item in sorted(ans):
    print(item)


#3.
def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1
    return cnt


print(hansu(int(input())))



