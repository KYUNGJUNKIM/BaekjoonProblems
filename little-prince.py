import math
T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        dist1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        dist2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)

        if cr > dist1 and cr > dist2:
            pass
        elif cr > dist1:
            cnt += 1
        elif cr > dist2:
            cnt += 1

    print(cnt)

