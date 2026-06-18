N, M = map(int,input().split())
G = [[] for _ in range(3*N)]
for _ in range(M):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    u0, u1, u2 = 3*u, 3*u+1, 3*u+2
    v0, v1, v2 = 3*v, 3*v+1, 3*v+2
    G[u0].append(v1)
    G[u1].append(v2)
    G[u2].append(v0)

S, T = map(int,input().split())
S, T = 3*(S-1), 3*(T-1)

from collections import deque

step = [0] * (3*N)
step[S] = 1
d = deque([S])

while d:
    u = d.popleft()
    for v in G[u]:
        if step[v]: continue
        d.append(v)
        step[v] = step[u] + 1
        if v == T: exit(print((step[v]-1)//3))

print(-1)