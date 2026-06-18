from collections import deque

N, M, S, T = map(int, input().split())
S, T = S-1, T-1
g = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    g[u].append((v, a, b))
    g[v].append((u, a, b))

inf = 10 ** 15
Yen = [inf] * N
Snk = [inf] * N
Yen[S] = 0
Snk[T] = 0

dqy = deque([S])
while dqy:
    u = dqy.popleft()
    for v, a, _ in g[u]:
        if Yen[v] > Yen[u] + a:
            Yen[v] = Yen[u] + a
            dqy.append(v)

dqs = deque([T])
while dqs:
    u = dqs.popleft()
    for v, _, b in g[u]:
        if Snk[v] > Snk[u] + b:
            Snk[v] = Snk[u] + b
            dqs.append(v)

Cost = [Yen[i] + Snk[i] for i in range(N)]
m = Cost[-1]
ans = [inf] * N
ans[-1] -= m

for i in range(1, N):
    m = min(m, Cost[-1-i])
    ans[-1-i] -= m

print(*ans, sep='\n')