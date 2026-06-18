N = int(input())
g = [[] for _ in range(N)]

for _ in range(N-1):
    u, v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

ans = N
for u in range(N):
    Y = [len(g[v])-1 for v in g[u] if v != u]
    Y.sort(reverse=True)
    for x in range(len(Y)):
        y = Y[x]
        ans = min(ans,N-1-(x+1)*(y+1))

print(ans)