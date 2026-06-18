from random import randint

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

M = 0
for _ in range(100):
    cnt = 0
    i = randint(0, N-1)
    while 1:
        j = randint(0, N-1)
        if j != i:
            break
    x1, y1 = P[i]
    x2, y2 = P[j]
    for x, y in P:
        if y * (x2 - x1) == (y2 - y1) * (x - x1) + y1 * (x2 - x1):
            cnt += 1
    M = max(M, cnt)

if M >= N - (N // 3) + 1:
    print(N - M)
else:
    print(N // 3)