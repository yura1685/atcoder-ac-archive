from collections import deque

N, M = map(int,input().split())

g = [[] for _ in range(N+1)]
c = [-1]*(N+1)
c[1] = 0

for _ in range(M):
    A, B = map(int,input().split())
    g[A].append(B)
    g[B].append(A)

d = deque([1])
while d:
    u = d.popleft()
    for v in g[u]:
        if c[v] == -1:
            c[v] = c[u] + 1
            d.append(v)

for i in range(1,N+1):
    print(c[i])