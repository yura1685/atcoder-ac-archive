from atcoder.dsu import DSU
from collections import defaultdict

N, K, L = map(int,input().split())

uf1 = DSU(N+1)
uf2 = DSU(N+1)
for _ in range(K):
    p, q = map(int,input().split())
    uf1.merge(p,q)
for _ in range(L):
    p, q = map(int,input().split())
    uf2.merge(p,q)

lead1 = [uf1.leader(x) for x in range(N+1)]
lead2 = [uf2.leader(x) for x in range(N+1)]

dd = defaultdict(int)
for i in range(N+1):
    dd[(lead1[i], lead2[i])] += 1

ans = [dd[(lead1[i], lead2[i])] for i in range(1,N+1)]
print(*ans)