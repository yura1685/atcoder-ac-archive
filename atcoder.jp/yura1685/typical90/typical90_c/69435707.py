from random import randint
from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
g = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(u):
    for v in g[u]:
        if dist[u] > dist[v]:
            continue
        dist[v] = dist[u] + 1
        dfs(v)
    
dist = [16851685] * N
p = randint(1,N-1)
dist[p] = 0
dfs(p)

m = 0
ind = 0

for i in range(N):
    if m <= dist[i]:
        m = dist[i]
        ind = i

dist = [16851685] * N
dist[ind] = 0
dfs(ind)

print(max(dist) + 1)