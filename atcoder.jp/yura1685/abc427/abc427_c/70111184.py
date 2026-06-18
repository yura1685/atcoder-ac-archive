from itertools import product

N, M = map(int,input().split())
g = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    g[u-1].add(v-1)

ans = 1685
for Perm in product([0,1],repeat=N):
    blue, red = [], []
    for i in range(N):
        (blue if Perm[i] else red).append(i)
    cnt = 0
    for i in blue:
        for j in blue:
            if i in g[j]:
                cnt += 1
    for i in red:
        for j in red:
            if i in g[j]:
                cnt += 1
    ans = min(ans, cnt)

print(ans)