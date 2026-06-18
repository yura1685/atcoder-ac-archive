# 第7回JOI予選 - 船旅

from atcoder.dsu import DSU
import heapq

n, k = map(int,input().split())
g = [[] for _ in range(n)]
dsu = DSU(n)

def price(x,y):
    A = [float('inf')]*n
    A[x] = 0
    P = [(0,x)]
    heapq.heapify(P)
    while P:
        w, u = heapq.heappop(P)
        d = {}
        for v, q in g[u]:
            if A[v] > w+q:
                A[v] = w+q
                d[v] = w+q
        for s in d:
            heapq.heappush(P,(d[s],s))
    return A[y]

for _ in range(k):
    q = list(map(int,input().split()))
    if q[0] == 1:
        c, d, e = q[1:]
        c, d = c-1, d-1
        dsu.merge(c,d)
        g[c].append((d,e))
        g[d].append((c,e))
    else:
        a, b = q[1]-1, q[2]-1
        if not dsu.same(a,b):
            print(-1)
        else:
            print(price(a,b))