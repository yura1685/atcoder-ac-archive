from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N + 2*M + 10)]
d = dict()
cnt = N
def f(st, co): return st * 998244353 + co
for _ in range(M):
    p, q, c = map(int, input().split())
    p, q = p-1, q-1
    if f(p, c) not in d:
        d[f(p, c)] = cnt
        g[p].append((cnt, 1))
        g[cnt].append((p, 0))
        cnt += 1
    if f(q, c) not in d:
        d[f(q, c)] = cnt
        g[q].append((cnt, 1))
        g[cnt].append((q, 0))
        cnt += 1

    p2 = d[f(p, c)]
    q2 = d[f(q, c)]
    g[p2].append((q2, 0))
    g[q2].append((p2, 0))

inf = 10 ** 18
dist = [inf] * cnt
dist[0] = 0
dq = deque([0])

while dq:
    u = dq.popleft()
    for v, w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            if w == 0:
                dq.appendleft(v)
            else:
                dq.append(v)

ans = dist[N-1]
print(ans if ans < inf else -1)