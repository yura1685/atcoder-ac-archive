from bisect import bisect, bisect_left

N, L = map(int,input().split())
D = list(map(int,input().split()))
point = [0]
for d in D:
    point.append((point[-1]+d)%L)
point.sort()
if L % 3 != 0:
    print(0)
    exit()
ans = 0
for p in point:
    if p >= L//3:
        break
    q = p + L//3
    r = p + L//3*2
    if bisect(point,q) != bisect_left(point,q) and bisect(point,r) != bisect_left(point,r):
        ans += (bisect(point,q) - bisect_left(point,q)) * ((bisect(point,r) - bisect_left(point,r)))
print(ans)