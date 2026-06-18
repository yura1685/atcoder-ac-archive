from sys import setrecursionlimit
setrecursionlimit(10**8)

N, M, L, S, T = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, C = map(int,input().split())
    g[U].append((V,C))

ans = set()
def dfs(u, depth, cost):
    if depth + 1 < L:
        for v, c in g[u]:
            if cost + c > T:
                continue
            dfs(v, depth+1, cost+c)
    else:
        for v, c in g[u]:
            if S <= cost + c <= T:
                ans.add(v)

dfs(1,0,0)

print(*sorted(ans))