from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**9)

N1, N2, M = map(int,input().split())

g = [[] for _ in range(N1+N2+1)]
for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

check = [0]*(N1+N2+1)
dis = [0]*(N1+N2+1)

check[1] = 1
check[N1+N2] = 1
def solve(d: deque):
    while d != deque():
        u = d.popleft()
        for v in g[u]:
            if check[v] == 0:
                check[v] = 1
                dis[v] = dis[u] + 1
                d.append(v)
            else:
                dis[v] = min(dis[v], dis[u]+1)

solve(deque([1]))
solve(deque([N1+N2]))
print(max(dis[:N1+1]) + max(dis[N1+1:]) + 1)