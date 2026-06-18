from atcoder.dsu import DSU

N = int(input())
uf = DSU(N+1)
E = []
for _ in range(N-1):
    u, v, w = map(int,input().split())
    E.append((u,v,w))

E.sort(key= lambda x: x[2])

ans = 0
for u, v, w in E:
    ans += w*uf.size(u)*uf.size(v)
    uf.merge(u,v)

print(ans)