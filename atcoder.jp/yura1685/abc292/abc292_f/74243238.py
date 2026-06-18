from math import sin, cos, pi

A, B = map(int, input().split())
A, B = min(A, B), max(A, B)
sq3 = 3 ** (1/2)

def f(rad):
    l = A / cos(rad)
    w = l * sin(rad + pi / 3)
    if w <= B:
        return True
    return False

l, r = 0, pi / 6
while r - l > 1e-12:
    mid = (l + r) / 2
    if f(mid):
        l = mid
    else:
        r = mid

print(A / cos(l))