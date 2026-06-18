from atcoder.dsu import DSU

N, Q = map(int,input().split())

uf = DSU(N+1)

for _ in range(Q):
    t, u, v = map(int,input().split())
    if t == 0: uf.merge(u, v)
    else: print(1 if uf.same(u, v) else 0)