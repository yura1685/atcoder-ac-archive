from atcoder.dsu import DSU
from collections import deque

N, M = map(int,input().split())
uf = DSU(N)
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    uf.merge(a,b)
    g[a].append(b)
    g[b].append(a)

gn = [-1] * N
cnt = 0
for ufg in uf.groups():
    gn[ufg[0]] = 2*cnt
    d = deque([ufg[0]])
    while d:
        u = d.popleft()
        for v in g[u]:
            if gn[v] >= 0:
                if gn[v] + gn[u] == 4*cnt + 1:
                    continue
                else:
                    exit(print(0))
            gn[v] = 4*cnt + 1 - gn[u]
            d.append(v)
    cnt += 1

gn_cnt = [0] * (2 * cnt)
for n in gn:
    gn_cnt[n] += 1

ans = 0
for u in range(N):
    ans += (N - gn_cnt[gn[u]] - len(g[u]))

print(ans//2)