from collections import deque

N, Q = map(int,input().split())
X = [0] + list(map(int, input().split()))
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

p = [0] * (N+1)
p[1] = 0
k = [0] * (N+1)
d = deque([1])
while d:
    u = d.popleft()
    for v in g[u]:
        if p[u] == v:
            continue
        d.append(v)
        p[v] = u
        k[u] += 1

ans = [[X[i]] for i in range(N+1)]

d = deque()
for i in range(1,N+1):
    if k[i] == 0:
        d.append(i)

while d:
    u = d.popleft()
    ans[u] = sorted(ans[u], reverse=True)[:20]
    ans[p[u]] += ans[u]
    k[p[u]] -= 1
    if k[p[u]] == 0: d.append(p[u])

for _ in range(Q):
    v, k = map(int,input().split())
    print(ans[v][k-1])