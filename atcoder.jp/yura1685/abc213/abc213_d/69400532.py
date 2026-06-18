from sortedcontainers import SortedList as SL
from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
g = [SL() for _ in range(N)]
for _ in range(N-1):
    A, B = map(int,input().split())
    g[A-1].add(B-1)
    g[B-1].add(A-1)

check = [0]*N
route = []

def dfs(u):
    route.append(u+1)
    while g[u]:
        v = g[u].pop(0)
        g[v].discard(u)
        dfs(v)
        route.append(u+1)

dfs(0)

print(*route)