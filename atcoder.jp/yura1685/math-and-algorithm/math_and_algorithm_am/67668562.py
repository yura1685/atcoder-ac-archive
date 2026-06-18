from sys import setrecursionlimit
setrecursionlimit(10**9)

N, M = map(int,input().split())

g = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    g[A].append(B)
    g[B].append(A)

check = [0]*(N+1)

def dfs(u):
    for v in g[u]:
        if check[v] == 0:
            check[v] = 1
            dfs(v)

check[1] = 1
dfs(1)

print('The graph is connected.' if sum(check) == N else 'The graph is not connected.')