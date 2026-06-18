from collections import defaultdict
from math import gcd

def Make_Perpendicular_Bisector(A,B):
    ax, ay, _ = A
    bx, by, _ = B
    a, b, c = 2*(bx-ax), 2*(by-ay), ax**2-bx**2+ay**2-by**2
    if a < 0:
        a, b, c = -a, -b, -c
    elif a == 0:
        if b < 0:
            b, c = -b, -c
        elif b == 0:
            if c < 0:
                c = -c
    g = gcd(a, b, c)
    return (a // g, b // g, c // g)

def Make_Midpoint(A, B):
    ax, ay, _ = A
    bx, by, _ = B
    return (ax + bx, ay + by)

N = int(input())
P = []
for _ in range(N):
    X, Y, C = map(int, input().split())
    P.append((X, Y, C))

D = defaultdict(dict)
for i in range(N):
    for j in range(i+1, N):
        a, b, c = Make_Perpendicular_Bisector(P[i], P[j])
        mx, my = Make_Midpoint(P[i], P[j])
        Cij = P[i][2] + P[j][2]
        C = D[(a, b, c)].get((mx, my))
        if C is None:
            D[(a, b, c)][(mx, my)] = Cij
        elif C < Cij:
            D[(a, b, c)][(mx, my)] = Cij

ans = -1
for d in D.values():
    m1, m2 = -1, -1
    for c in d.values():
        if c >= m1:
            m1, m2 = c, m1
        elif m1 > c >= m2:
            m2 = c
    if m2 >= 0:
        ans = max(ans, m1 + m2)

print(ans)