from atcoder.dsu import DSU

N, M = map(int, input().split())
uf = DSU(N)
ans = N
for _ in range(M):
    x, y, z = map(int, input().split())
    if not uf.same(x-1, y-1):
        uf.merge(x-1, y-1)
        ans -= 1
        
print(ans)