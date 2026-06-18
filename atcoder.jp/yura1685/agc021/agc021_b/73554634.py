from collections import defaultdict
from math import atan2, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross_product(a, b, c):
    """外積を計算: 正なら左回り、負なら右回り、0なら直線上"""
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def get_convex_hull(points):
    n = len(points)
    if n <= 2:
        return points

    sorted_points = sorted(points, key=lambda p: (p.x, p.y))

    hull = []

    for p in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    lower_size = len(hull)
    for i in range(n - 2, -1, -1):
        p = sorted_points[i]
        while len(hull) > lower_size and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    hull.pop()
    
    return hull

def Make_Perpendicular_Bisector(A,B):
    ax, ay = A.x, A.y
    bx, by = B.x, B.y
    return (bx-ax, by-ay, (ax**2-bx**2+ay**2-by**2)/2)

N = int(input())
P = []
points = []
for _ in range(N):
    x, y = map(int,input().split())
    P.append((x,y))
    points.append(Point(x,y))

hull = get_convex_hull(points)
hull = [hull[-1]] + hull + [hull[0]]
H = len(hull)

d = defaultdict(float)

for m in range(1,H-1):
    l, r = m-1, m+1
    a1, b1, c1 = Make_Perpendicular_Bisector(hull[l], hull[m])
    a2, b2, c2 = Make_Perpendicular_Bisector(hull[m], hull[r])
    arg1 = atan2(-a1,b1)
    arg2 = atan2(-a2,b2)
    arg = (arg2 - arg1) % (2*pi)
    d[(hull[m].x, hull[m].y)] = arg / (2*pi)

for x, y in P:
    print(d[(x,y)])