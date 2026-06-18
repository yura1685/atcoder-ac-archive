from atcoder.dsu import DSU

N, Q = map(int,input().split())
g = DSU(N+1)
for _ in range(Q):
    t, a, b = map(int,input().split())
    if t == 1:
        g.merge(a,b)
    else:
        print('Yes' if g.same(a,b) else 'No')