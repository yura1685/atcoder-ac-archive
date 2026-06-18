from atcoder.dsu import DSU
from collections import deque

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
g = [[] for _ in range(N+1)]
dsu = DSU(N+1)

for i in range(M):
    a, b = A[i], B[i]
    g[a].append(b)
    g[b].append(a)
    dsu.merge(a,b)

ans = [-1] * (N+1)

Groups = dsu.groups()
for Gs in Groups:
    ans[Gs[0]] = 1
    d = deque([Gs[0]])
    while d:
        u = d.popleft()
        for v in g[u]:
            if ans[v] == -1:
                ans[v] = ans[u]^1
                d.append(v)
            elif ans[v] == ans[u]:
                exit(print('No'))
print('Yes')