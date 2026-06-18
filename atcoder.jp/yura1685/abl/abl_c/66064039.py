from atcoder.dsu import DSU

N, M = map(int,input().split())

town = DSU(N+1)

for _ in range(M):
    A, B = map(int,input().split())
    town.merge(A,B)

n = len(town.groups())    
print(n-2)