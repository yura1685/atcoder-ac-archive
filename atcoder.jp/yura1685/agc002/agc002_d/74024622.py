from atcoder.dsu import DSU
from collections import defaultdict

N, M = map(int, input().split())
E: list[tuple[int, int]] = [(0, 0)]
for i in range(1, M+1):
    a, b = map(int, input().split())
    E.append((a, b))

Q = int(input())
query = []
for _ in range(Q):
    x, y, z = map(int, input().split())
    query.append((x, y, z))

ans = [-1] * Q
d = defaultdict(list)
for i in range(Q):
    d[(0, M)].append(i)

while d:
    d2 = defaultdict(list)
    mids = defaultdict(list)
    for (ng, ok), Lst in d.items():
        mid = (ng + ok) // 2
        mids[mid].append((ng, ok, Lst))
    
    uf = DSU(N+1)
    now = 0
    for mid in sorted(mids.keys()):
        while now < mid:
            now += 1
            a, b = E[now]
            uf.merge(a, b)
    
        for ng, ok, Lst in mids[mid]:
            for i in Lst:
                x, y, z = query[i]
                cnt = 0
                if uf.same(x, y):
                    cnt = uf.size(x)
                else:
                    cnt = uf.size(x) + uf.size(y)

                if cnt >= z:
                    if mid - ng <= 1:
                        ans[i] = mid
                    else:
                        d2[(ng, mid)].append(i)
                else:
                    if ok - mid <= 1:
                        ans[i] = ok
                    else:
                        d2[(mid, ok)].append(i)
    d = d2

for a in ans:
    print(a)