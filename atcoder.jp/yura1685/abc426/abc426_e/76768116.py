from math import hypot

def move(x1, y1, x2, y2, k):
    return x1 * (1 - k) + x2 * k, y1 * (1 - k) + y2 * k

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

def dist_segment_point(x1, y1, x2, y2, x3, y3):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return hypot(x3 - x1, y3 - y1)
    ap_x, ap_y = x3 - x1, y3 - y1
    bp_x, bp_y = x3 - x2, y3 - y2
    if dx * ap_x + dy * ap_y < 0:
        return hypot(ap_x, ap_y)
    if (-dx) * bp_x + (-dy) * bp_y < 0:
        return hypot(bp_x, bp_y)
    return abs(dx * ap_y - dy * ap_x) / hypot(dx, dy)

def solve():
    tsx, tsy, tgx, tgy = map(int, input().split())
    asx, asy, agx, agy = map(int, input().split())
    time_t = dist(tsx, tsy, tgx, tgy)
    time_a = dist(asx, asy, agx, agy)
    if time_t > time_a:
        tsx, tsy, tgx, tgy, asx, asy, agx, agy = asx, asy, agx, agy, tsx, tsy, tgx, tgy
        time_t, time_a = time_a, time_t
    ans = 1685
    l, r = 0, time_t
    while r - l > 1e-8:
        mid1, mid2 = (2 * l + r) / 3, (l + 2 * r) / 3
        if (dist(*move(tsx, tsy, tgx, tgy, mid1 / time_t),
                *move(asx, asy, agx, agy, mid1 / time_a)) <
            dist(*move(tsx, tsy, tgx, tgy, mid2 / time_t),
                *move(asx, asy, agx, agy, mid2 / time_a))):
            r = mid2
        else:
            l = mid1
    ans = min(ans, dist(*move(tsx, tsy, tgx, tgy, l / time_t), *move(asx, asy, agx, agy, l / time_a)))
    ans = min(ans, dist_segment_point(*move(asx, asy, agx, agy, time_t / time_a), agx, agy, tgx, tgy))
    print(ans)

for _ in range(int(input())):
    solve()