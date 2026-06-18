from math import pi

N, Q = map(int, input().split())
Cones = [list(map(int, input().split())) for _ in range(N)]

def volume(r, h):
    return r * r * pi * h / 3

for _ in range(Q):
    I = input().split()
    A, B = int(I[0]), int(I[1])
    ans = 0
    for x, r, h in Cones:
        if B <= x or x + h <= A:
            continue
        if x < A:
            r = r * (h - A + x) / h
            h = h - A + x 
            x = A
        if x + h <= B:
            ans += volume(r, h)
        else:
            r2 = r * (h - B + x) / h
            h2 = h - (B - x)
            ans += volume(r, h) - volume(r2, h2)
    print(ans)