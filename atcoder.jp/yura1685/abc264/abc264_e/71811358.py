from atcoder.dsu import DSU

N, M, E = map(int,input().split())
lines = []
g = [[] for _ in range(N+M)]
for _ in range(E):
    U, V = map(int,input().split())
    g[U-1].append(V-1)
    g[V-1].append(U-1)
    lines.append((U-1, V-1))
Q = int(input())
query = [int(input())-1 for _ in range(Q)]
now = set([i for i in range(E)]) - set(query)

ok = [0] * N + [1] * M
uf = DSU(N+M)
for x in now:
    u, v = lines[x]
    flag = 0
    if ok[uf.leader(u)] or ok[uf.leader(v)]: flag = 1
    uf.merge(u,v)
    if flag: ok[uf.leader(u)] = 1

s = sum([ok[uf.leader(i)] for i in range(N)])
ans = [s]
query.reverse()

for e in query:
    u, v = lines[e]
    p = uf.leader(u)
    q = uf.leader(v)
    if ok[p] ^ ok[q]:
        if ok[p]:
            s += uf.size(v)
        else:
            s += uf.size(u)
        ok[p] = 1
        ok[q] = 1
    uf.merge(u,v)
    ans.append(s)

for i in range(Q-1,-1,-1): print(ans[i])