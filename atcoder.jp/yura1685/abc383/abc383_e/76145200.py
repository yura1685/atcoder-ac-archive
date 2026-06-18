from atcoder.dsu import DSU

N, M, K = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]
E.sort(key=lambda x: x[2])
A, B = [0] * (N+1), [0] * (N+1)
for a in input().split():
    A[int(a)] += 1
for b in input().split():
    B[int(b)] += 1

ans = 0
uf = DSU(N+1)

for x, y, w in E:
    u, v = uf.leader(x), uf.leader(y)
    if u == v: continue
    au, bu = A[u], B[u]
    av, bv = A[v], B[v]
    if au and bv:
        m = min(au, bv)
        ans += m * w
        au, bv = au-m, bv-m
    if bu and av:
        m = min(bu, av)
        ans += m * w
        bu, av = bu-m, av-m
    uf.merge(u, v)
    z = uf.leader(u)
    if z == u:
        A[u] = au + av
        B[u] = bu + bv
    else:
        A[v] = au + av
        B[v] = bu + bv

print(ans)