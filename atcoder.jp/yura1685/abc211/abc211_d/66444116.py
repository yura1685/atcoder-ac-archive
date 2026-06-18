from collections import deque

N, M = map(int,input().split())
mod = 10**9 + 7
g = [[] for _ in range(N+1)]
c = [-1]*(N+1)
pat = [0]*(N+1)
pat[1] = 1
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
            d.append(v)
            c[v] = c[u] + 1
            pat[v] += pat[u]
            pat[v] %= mod
        elif c[v] == c[u] + 1:
            pat[v] += pat[u]
            pat[v] %= mod

print(pat[-1]%mod)