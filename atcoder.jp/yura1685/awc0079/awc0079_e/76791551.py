from math import gcd
from collections import defaultdict

mod = 10 ** 9 + 7
d = defaultdict(int)
cnt = 0
N = int(input())
for _ in range(N):
    K = int(input())
    if K > 2:
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        dx, dy = x2 - x1, y2 - y1
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        nx, ny = x2, y2
        flag = True
        for _ in range(K-2):
            x, y = map(int, input().split())
            cx, cy = x - nx, y - ny
            g = gcd(cx, cy)
            if cx // g == dx and cy // g == dy:
                nx, ny = x, y
            else:
                flag = False
        if flag:
            if dx < 0: dx, dy = -dx, -dy
            if dx == 0: dy = abs(dy)
            d[(dx, dy)] += 1
    elif K == 1:
        cnt += 1
        _ = input()
    else:
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        dx, dy = x2 - x1, y2 - y1
        if dx < 0: dx, dy = -dx, -dy
        elif dx == 0: dy = abs(dy)
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        d[(dx, dy)] += 1

pw = pow(2, cnt, mod)
ans = pw - 1
for _, n in d.items():
    ans += pw * (pow(2, n, mod) - 1) % mod
    ans %= mod
ans = (pow(2, N, mod) - 1 - ans)
print(ans % mod)