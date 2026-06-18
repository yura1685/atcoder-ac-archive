N, M = map(int,input().split())
g = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    g[a][b] = 1
    g[b][a] = 1

from itertools import permutations

ans = 1685
for P in permutations([i for i in range(N)]):
    new = 0
    for i in range(N):
        a, b = P[i], P[(i+1)%N]
        if not g[a][b]: new += 1
    ans = min(ans, M - N + 2*new)
    if N <= 5: continue
    new = 0
    P1, P2 = P[:3], P[3:]
    for i in range(3):
        a, b = P1[i], P1[(i+1)%3]
        if not g[a][b]: new += 1
    for i in range(N-3):
        a, b = P2[i], P2[(i+1)%(N-3)]
        if not g[a][b]: new += 1
    ans = min(ans, M - N + 2*new)
    if N <= 7: continue
    new = 0
    P1, P2 = P[:4], P[4:]
    for i in range(4):
        a, b = P1[i], P1[(i+1)%4]
        if not g[a][b]: new += 1
    for i in range(4):
        a, b = P2[i], P2[(i+1)%4]
        if not g[a][b]: new += 1
    ans = min(ans, M - N + 2*new)

print(ans)