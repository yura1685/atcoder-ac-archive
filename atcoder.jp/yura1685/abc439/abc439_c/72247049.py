from math import isqrt

N = int(input())

s, t = set(), set()

for x in range(1,N):
    if 2*x*x >= N: break
    for y in range(x+1,N):
        P = x*x + y*y
        if P > N: break
        if P in s: t.add(P)
        else: s.add(P)

L = sorted(s-t)
print(len(L))
print(*L)