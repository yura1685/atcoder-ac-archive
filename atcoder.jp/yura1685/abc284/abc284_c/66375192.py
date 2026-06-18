N, M = map(int,input().split())

g = [[] for _ in range(N)]
c = [0]*N

def dfs(u):
    for v in g[u]:
        if c[v] == 0:
            c[v] = 1
            dfs(v)

for _ in range(M):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    g[u].append(v)
    g[v].append(u)

ans = 0
for i in range(N):
    if c[i] == 0:
        ans += 1
        c[i] = 1
        dfs(i)

print(ans)