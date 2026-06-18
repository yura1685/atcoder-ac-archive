from itertools import permutations
from collections import defaultdict

N, M = map(int,input().split())
g = [[0]*N for _ in range(N)]

for _ in range(M):
    A, B, C = map(int,input().split())
    g[A-1][B-1] = C
    g[B-1][A-1] = C

ans = 0
for p in permutations([i for i in range(N)]):
    cnt = 0
    now = p[0]
    for i in range(1,N):
        if not g[now][p[i]]:
            break
        cnt += g[now][p[i]]
        now = p[i]
    ans = max(ans,cnt)

print(ans)