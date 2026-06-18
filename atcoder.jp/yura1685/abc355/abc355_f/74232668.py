from atcoder.dsu import DSU

N, Q = map(int, input().split())
C = [N] * 9
G = [DSU(N) for _ in range(9)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    for i in range(c-1, 9):
        g = G[i]
        if not g.same(a, b):
            g.merge(a, b)
            C[i] -= 1

for _ in range(Q):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    for i in range(w-1, 9):
        g = G[i]
        if not g.same(u, v):
            g.merge(u, v)
            C[i] -= 1
    print(N + sum(C) - 10)
