import math

N, K = map(int, input().split())
Ps = [tuple(map(int, input().split())) for _ in range(N)]

def Intersections(x1, y1, r1, x2, y2, r2):
    d = math.hypot(x2 - x1, y2 - y1)
    if d > r1 + r2 or d < abs(r1 - r2) or (d == 0 and r1 == r2):
        return []
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0.0, r1**2 - a**2))
    px = x1 + a * (x2 - x1) / d
    py = y1 + a * (y2 - y1) / d
    ix1 = px + h * (y2 - y1) / d
    iy1 = py - h * (x2 - x1) / d
    ix2 = px - h * (y2 - y1) / d
    iy2 = py + h * (x2 - x1) / d
    if math.isclose(d, r1 + r2) or math.isclose(d, abs(r1 - r2)):
        return [(px, py)]
    return [(ix1, iy1), (ix2, iy2)]

def solve(t):
    P = [(x, y) for x, y, _ in Ps]
    for i in range(N):
        for j in range(i+1, N):
            xi, yi, ci = Ps[i]
            xj, yj, cj = Ps[j]
            P += Intersections(xi, yi, t/ci, xj, yj, t/cj)
    for x, y in P:
        cnt = 0
        for x2, y2, c2 in Ps:
            if (x - x2) ** 2 + (y - y2) ** 2 <= (t / c2) ** 2 + 1e-7:
                cnt += 1
        if cnt >= K:
            return True
    return False

ng, ok = 0, 1e10
while ok - ng > 1e-8:
    mid = (ng + ok) / 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)