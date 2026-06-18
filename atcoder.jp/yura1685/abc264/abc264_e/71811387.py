from atcoder.dsu import DSU

N, M, E = map(int,input().split())
lines = []
g = [[] for _ in range(N+1)]
for _ in range(E):
    U, V = map(int,input().split())
    if U > N: U = 0
    if V > N: V = 0
    g[U].append(V)
    g[V].append(U)
    lines.append((U,V))
Q = int(input())
query = [int(input())-1 for _ in range(Q)]
now = set([i for i in range(E)]) - set(query)

uf = DSU(N+1)
for x in now:
    u, v = lines[x]
    uf.merge(u,v)

ans = [uf.size(0)-1]
query.reverse()

for e in query:
    u, v = lines[e]
    uf.merge(u,v)
    ans.append(uf.size(0)-1)

for i in range(Q-1,-1,-1): print(ans[i])