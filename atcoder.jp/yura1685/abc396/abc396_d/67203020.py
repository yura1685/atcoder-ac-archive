N, M = map(int,input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int,input().split())
    g[u-1].append((v-1,w))
    g[v-1].append((u-1,w))

route = []

def dfs(u,path,weight):
    if u == N-1:
        route.append((path,weight))
        return  
    for v, w in g[u]:
        if v not in path:
            dfs(v,path+[v],weight+[w])

dfs(0,[0],[])

ans = float('inf')
for P, W in route:
    x = 0
    for w in W:
        x ^= w
    ans = min(ans,x)

print(ans)