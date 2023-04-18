#1. 너의 평점은(25206)
# score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
# scores = []
# times = []
# total = 0
#
# for i in range(20):
#     info = input()
#     if info[-1] == 'P':
#         continue
#     elif info[-1] == 'F':
#         scores.append(0)
#         time = float(info[::-1][3:6][::-1])
#         times.append(time)
#     else:
#         score = score_dict[info[: -3:-1][::-1]]
#         time = float(info[::-1][3:6][::-1])
#         scores.append(score)
#         times.append(time)
# # print(scores)
# # print(times)
# for i in range(len(scores)):
#     total += scores[i] * times[i]
# print(total/sum(times))


#2. 팰린드롬인지 확인하기(10988)
# word = input()
# median = len(word)//2
# flag = 1
# for i in range(median+1):
#     if word[i] != word[-1-i]:
#         flag = 0
#         break
# print(flag)


#3. 바구니 순서 바꾸기(10812)
# n, m = map(int, input().split())
# nums = [i for i in range(n+1)]
#
# for _ in range(m):
#     i, j, k = map(int, input().split())
#     nums[i:j+1] = nums[k:j+1] + nums[i:k]
# for x in range(1, len(nums)):
#     print(nums[x], end=' ')


#4. 별찍기(2444)
# n = int(input())
# for i in range(1, n):
#     print(' '*(n-i)+'*'*(2*i-1))
# for i in range(n, 0, -1):
#     print(' '*(n-i)+'*'*(2*i-1))


#5. 퀸, 킹, 룩, 비숍(3003)
# my = list(map(int, input().split()))
# sets = [1, 1, 2, 2, 2, 8]
# result = [a - b for a, b in zip(sets, my)]
# for i in result:
#     print(i, end=' ')


#6.












