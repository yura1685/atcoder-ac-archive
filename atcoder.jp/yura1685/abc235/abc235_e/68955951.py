from atcoder.dsu import DSU

N, M, Q = map(int,input().split())
query = []
for _ in range(M):
    a, b, c = map(int,input().split())
    query.append((c,a,b,-1))
for i in range(Q):
    u, v, w = map(int,input().split())
    query.append((w,u,v,i))
query.sort()

ans = [False] * Q

uf = DSU(N+1)
for w, u, v, i in query:
    if i == -1:
        if not uf.same(u,v):
            uf.merge(u,v)
    else:
        if not uf.same(u,v):
            ans[i] = True

for i in ans:
    print('Yes' if i else 'No')