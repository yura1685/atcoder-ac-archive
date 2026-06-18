from math import gcd

def extended_euclid(a, b):
    if b == 0:
        return (1, 0)
    else:
        xd, yd = extended_euclid(b, a % b)
        return (yd, xd - a // b * yd)

X, Y = map(int,input().split())

g = gcd(X,Y)
if g > 2:
    exit(print(-1))

# AY + BX = 1 を満たす A, B
A, B = extended_euclid(Y, X)

for x, y in [(1,1),(1,-1),(-1,1),(-1,-1),
             (2,2),(2,-2),(-2,2),(-2,-2)]:
    if abs(A*y*Y - B*x*X) == 2:
        exit(print(A*y, B*x))