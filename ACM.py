from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))  # 건물 올리는 시간
    rules = [[] for _ in range(N + 1)]  # 건물규칙
    indegree = [0 for _ in range(N + 1)]  # 진입차수
    result = [0 for _ in range(N + 1)]
    for i in range(K):
        a, b = map(int, input().split())
        rules[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i]

    while q:
        a = q.popleft()
        for i in rules[a]:
            indegree[i] -= 1
            result[i] = max(result[a] + cost[i], result[i])
            if indegree[i] == 0:
                q.append(i)

    answer = int(input())
    print(result[answer])


