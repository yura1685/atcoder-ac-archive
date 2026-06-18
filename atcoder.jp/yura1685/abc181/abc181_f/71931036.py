from atcoder.dsu import DSU
from functools import cache

N = int(input())
P = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,y))

@cache
def d(A,B):
    if A > B: A, B = B, A
    if A == 0 and B == N+1: return 200
    if A == 0: return 100 - P[B-1][1]
    if B == N+1: return P[A-1][1] + 100
    A, B = A-1, B-1
    return ((P[A][0]-P[B][0])**2 + (P[A][1]-P[B][1])**2) ** (1/2)

def f(r): # 半径rは達成可能か？
    uf = DSU(N+2)
    for i in range(N+1):
        for j in range(N+2):
            if d(i,j) < 2*r:
                uf.merge(i,j)
    if uf.same(0,N+1): return False
    return True

l, r = 0, 100
while abs(r-l) > 1e-7:
    mid = (l+r)/2
    if f(mid): l = mid
    else: r = mid

print(r)