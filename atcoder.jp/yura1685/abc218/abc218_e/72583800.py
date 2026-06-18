from atcoder.dsu import DSU

N, M = map(int,input().split())
ans = 0
uf = DSU(N+1)
E = []
for _ in range(M):
    a, b, c = map(int,input().split())
    if c < 0:
        uf.merge(a,b)
    else:
        ans += c
        E.append((c,a,b))

E.sort()

for c, a, b in E:
    if not uf.same(a,b):
        uf.merge(a,b)
        ans -= c

print(ans)