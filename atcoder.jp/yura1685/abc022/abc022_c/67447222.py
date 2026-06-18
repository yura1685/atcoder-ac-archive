N, M = map(int,input().split())
g = [[float('inf')]*N for _ in range(N)]
p = [float('inf')]*N
ind = []
for _ in range(M):
    u, v, l = map(int,input().split())
    if u == 1:
        p[v-1] = l
        ind.append(v-1)   
        continue     
    g[u-1][v-1] = l
    g[v-1][u-1] = l

for i in range(N):
    g[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i*j*k == 0:
                continue
            g[i][j] = min(g[i][j],g[i][k] + g[k][j])

ans = float('inf')
for i in range(len(ind)-1):
    for j in range(i+1,len(ind)):
        ans = min(ans,g[ind[i]][ind[j]] + p[ind[i]] + p[ind[j]])

print(ans if ans < float('inf') else -1)