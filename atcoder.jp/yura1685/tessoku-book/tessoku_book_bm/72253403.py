from sys import setrecursionlimit
from functools import cache
setrecursionlimit(10**6)

N = int(input())
A = [int(x) - 1 for x in input().split()]
c = [False] * N
g = [[] for _ in range(N)]
for i in range(N-1):
    g[A[i]].append(i+1)
    c[A[i]] = True

@cache
def dfs(u):
    if not c[u]: return 0
    buka = 0
    for v in g[u]:
        buka += dfs(v) + 1
    return buka

print(*[dfs(i) for i in range(N)])