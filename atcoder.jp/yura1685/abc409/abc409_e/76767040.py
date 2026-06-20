N = int(input())
X = list(map(int, input().split()))
g:list[list[tuple[int, int]]] = [[] for _ in range(N)]
for _ in range(N-1):
    I = input().split()
    u, v, w = int(I[0]), int(I[1]), int(I[2])
    g[u-1].append((v-1, w))
    g[v-1].append((u-1, w))

visit:list[bool] = [False] * N
ans = 0
def dfs(u:int, c:int) -> int:
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