from sys import setrecursionlimit
setrecursionlimit(10**6)
N = int(input())

g = [[] for _ in range(N)]
g[0].append(-1)
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

cnt = [0] * N

def dfs(u, p):
    if len(g[u]) == 1:
        cnt[u] = 0
        return 0
    res = 0
    for v in g[u]:
        if v == p:
            continue
        res += dfs(v, u) + 1
    cnt[u] = res
    return res

dfs(0, -1)

def dfs2(u, p):
    if len(g[u]) == 1:
        return 0
    res = 0
    for v in g[u]:
        if v == p:
            continue
        res += dfs2(v, u) + (cnt[v] + 1) * (N - cnt[v] - 1)
    return res

print(dfs2(0, -1))