from atcoder.dsu import DSU

N, M = map(int,input().split())

g = DSU(N+1)

for _ in range(M):
    A, B = map(int,input().split())
    g.merge(A,B)

print('The graph is connected.' if len(g.groups()) == 2 else 'The graph is not connected.')