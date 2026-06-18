from atcoder.dsu import DSU

N, M = map(int,input().split())
g = DSU(N+1)
for _ in range(M):
    a, b = map(int,input().split())
    g.merge(a,b)

print(len(g.groups())-2)