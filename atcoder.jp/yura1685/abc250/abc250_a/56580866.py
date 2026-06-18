h, w = map(int,input().split())
r, c = map(int,input().split())
ans = 0
if 1 < r:
    ans += 1
if r < h:
    ans += 1
if 1 < c:
    ans += 1
if c < w:
    ans += 1
print(ans)