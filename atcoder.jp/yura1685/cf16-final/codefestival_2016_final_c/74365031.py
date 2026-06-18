from atcoder.dsu import DSU

N, M = map(int, input().split())
uf = DSU(M+N+1)
for i in range(1, N+1):
    K, *L = map(int, input().split())
    u = i + M
    for v in L:
        uf.merge(u, v)

u = M + 1
for v in range(M+2, M+N+1):
    if not uf.same(u, v):
        print('NO')
        break
else:
    print('YES')