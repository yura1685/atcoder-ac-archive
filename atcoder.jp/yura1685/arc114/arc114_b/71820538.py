from atcoder.dsu import DSU

N = int(input())
F = [int(x)-1 for x in input().split()]
C = [True] * N
for f in F: C[f] = False
for i in range(N):
    if C[i]: F[i] = -1

uf = DSU(N)
for i in range(N):
    if F[i] == -1: continue
    uf.merge(i,F[i])

val = len(uf.groups()) - sum(C)
print(pow(2,val,998244353)-1)