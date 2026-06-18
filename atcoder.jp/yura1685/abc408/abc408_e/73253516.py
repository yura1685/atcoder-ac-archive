from atcoder.dsu import DSU

N, M = map(int,input().split())
G = []
for _ in range(M):
    u, v, w = map(int,input().split())
    G.append((u-1,v-1,w))

x = (1 << 30) - 1

for k in range(29,-1,-1):
    x ^= 1 << k
    uf = DSU(N)
    for u, v, w in G:
        if x | w == x:
            uf.merge(u,v)
    if not uf.same(0,N-1):
        x ^= 1 << k

print(x)