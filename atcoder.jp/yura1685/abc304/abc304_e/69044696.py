from atcoder.dsu import DSU

N, M = map(int,input().split())
uf = DSU(N+1)
s = set()

for _ in range(M):
    u, v = map(int,input().split())
    uf.merge(u,v)

K = int(input())
for _ in range(K):
    x, y = map(int,input().split())
    a, b = uf.leader(x), uf.leader(y)
    s.add((min(a,b), max(a,b)))

Q = int(input())
for _ in range(Q):
    p, q = map(int,input().split())
    a, b = uf.leader(p), uf.leader(q)
    print('No' if (min(a,b), max(a,b)) in s else 'Yes')