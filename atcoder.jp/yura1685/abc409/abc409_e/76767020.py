from sys import setrecursionlimit
setrecursionlimit(100010)

N = int(input())
X = list(map(int, input().split()))
g = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    g[u-1].append((v-1, w))
    g[v-1].append((u-1, w))

visit = [False] * N
ans = 0
def dfs(u, c):
    x = X[u]
    for v, w in g[u]:
        if visit[v]:
            continue
        visit[v] = True
        x += dfs(v, w)
    global ans
    ans += abs(x) * c
    return x

visit[0] = True
dfs(0, 0)
print(ans)