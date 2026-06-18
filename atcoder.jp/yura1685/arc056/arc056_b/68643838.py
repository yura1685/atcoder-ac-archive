from atcoder.dsu import DSU

N, M, S = map(int,input().split())
dsu = DSU(N+1)
edge = []
for _ in range(M):
    u, v = map(int,input().split())
    edge.append((min(u,v), max(u,v)))
edge.sort(reverse=True)

i = 0
ans = []
for u in range(N,0,-1):
    while i < M and edge[i][0] == u:
        dsu.merge(edge[i][0],edge[i][1])
        i += 1
    if dsu.same(S,u):
        ans.append(u)

for a in ans[::-1]:
    print(a)