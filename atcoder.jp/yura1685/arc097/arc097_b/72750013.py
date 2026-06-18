from atcoder.dsu import DSU

N, M = map(int,input().split())
P = list(map(int,input().split()))
uf = DSU(N+1)

for _ in range(M):
    x, y = map(int,input().split())
    uf.merge(x,y)

ans = 0
for g in uf.groups()[1:]:
    s1, s2 = set(), set()
    for u in g:
        s1.add(u)
        s2.add(P[u-1])
    ans += len(s1 & s2)
print(ans)