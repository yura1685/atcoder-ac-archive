from collections import deque

N, Q = map(int,input().split())

g = [[] for _ in range(N+1)]
dis = [-1]*(N+1)
dis[1] = 0
d = deque([1])

for _ in range(N-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

while d:
    u = d.popleft()
    for v in g[u]:
        if dis[v] == -1:
            d.append(v)
            dis[v] = dis[u] + 1

for _ in range(Q):
    c, d = map(int,input().split())
    print('Town' if (dis[c]-dis[d]) % 2 == 0 else 'Road')