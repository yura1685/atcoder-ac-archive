from math import isqrt
e4 = 10000
X_, Y_, R_ = map(float,input().split())
if X_ < 0: X_ = -X_
if Y_ < 0: Y_ = -Y_
X, Y, R = int(e4*X_+0.5) % e4, int(e4*Y_+0.5) % e4, int(e4*R_+0.5)
l = X - R
r = X + R
if l % e4:
    l = (l - l % e4) + e4
if r % e4:
    r = r - r % e4

ans = 0
for x in range(l, r+1, e4):
    c = isqrt(R ** 2 - (X-x) ** 2)
    d, u = c - Y, c + Y
    ans += u // e4 + max(0, d // e4)
    if d >= 0:
        ans += 1

print(ans)