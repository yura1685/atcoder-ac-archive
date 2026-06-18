ax, ay = map(int,input().split())
bx, by = map(int,input().split())
cx, cy = map(int,input().split())

def naibun(n): # B:C を k:1-k に内分した点とAとの距離の2乗
    return ((1-n)*bx + n*cx - ax)**2 + ((1-n)*by + n*cy - ay)**2

l, r = 0, 1
for _ in range(100):
    if naibun(l) <= naibun(r):
        r = (l+r)/2
    else:
        l = (l+r)/2

print(naibun(l)**(1/2))