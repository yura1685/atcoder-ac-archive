from atcoder.dsu import DSU

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
g = DSU(N)

for _ in range(M):
    c, d = map(int,input().split())
    g.merge(c-1,d-1)

for groups in g.groups():
    if sum(A[a] for a in groups) != sum(B[b] for b in groups):
        exit(print('No'))
print('Yes')