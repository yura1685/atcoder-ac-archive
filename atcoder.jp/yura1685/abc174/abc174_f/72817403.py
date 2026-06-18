from atcoder.fenwicktree import FenwickTree
from collections import defaultdict

N, Q = map(int,input().split())
C = [0] + list(map(int,input().split()))
ft = FenwickTree(N+1)

query = defaultdict(list)
for i in range(Q):
    l, r = map(int,input().split())
    query[r].append((l,i))

ans = [0] * Q
ind = [0] * (N+1)

for r in range(1,N+1):
    ft.add(ind[C[r]],-1)
    ind[C[r]] = r
    ft.add(r,1)
    if query[r]:
        for l, i in query[r]:
            ans[i] = ft.sum(l,r+1)

for a in ans:
    print(a)