N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def dfs(lst, p):
    L = [(p,-1)]
    while L:
        u, f = L.pop()
        lst[u] = lst[f] + 1
        for v in g[u]:
            if lst[v] != -1:
                continue
            L.append((v,u))

d0 = [-1] * (N+1)
dfs(d0, 0)
u = max([(d0[i],i) for i in range(N)])[1]
du = [-1] * (N+1)
dfs(du, u)
v = max([(du[i],i) for i in range(N)])[1]
dv = [-1] * (N+1)
dfs(dv, v)

for i in range(N):
    print(max((du[i], u),(dv[i], v))[1] + 1)