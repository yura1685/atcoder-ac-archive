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

    # 1. ソート (xを優先、次にyで昇順)
    # Pythonのsortは安定ソートで、Pointオブジェクトもタプルとして扱えば簡単にソートできます
    sorted_points = sorted(points, key=lambda p: (p.x, p.y))

    hull = []

    # 2. Lower-hull (下側凸包) の構築
    for p in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    # 3. Upper-hull (上側凸包) の構築
    lower_size = len(hull)
    for i in range(n - 2, -1, -1):
        p = sorted_points[i]
        while len(hull) > lower_size and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    # 最後の点は最初の点と重複するため削除
    hull.pop()
    
    return hull

P = [tuple(map(int,input().split())) for _ in range(4)]
points = [Point(x,y) for x,y in P]
hull = get_convex_hull(points)

print('Yes' if len(hull) == 4 else 'No')