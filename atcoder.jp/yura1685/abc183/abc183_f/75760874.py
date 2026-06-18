from collections import defaultdict
from atcoder.dsu import DSU
N, Q = map(int, input().split())
C = list(map(int, input().split()))
D = [defaultdict(int) for _ in range(N)]
for i, c in enumerate(C): D[i][c] += 1
uf = DSU(N)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a, b = q[1] - 1, q[2] - 1
        if uf.same(a, b):
            continue
        u, v = uf.leader(a), uf.leader(b)
        uf.merge(u, v)
        w = uf.leader(u)
        if w == u:
            for c, n in D[v].items():
                D[u][c] += n
            D[v].clear()
        else:
            for c, n in D[u].items():
                D[v][c] += n
            D[u].clear()
    
    else:
        x, y = q[1] - 1, q[2]
        print(D[uf.leader(x)][y])
