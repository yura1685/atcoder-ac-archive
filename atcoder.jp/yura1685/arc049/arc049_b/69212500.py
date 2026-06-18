N = int(input())
XYC = [tuple(map(int,input().split())) for _ in range(N)]

l, r = 0, 10 ** 10

for _ in range(100):
    t = (l+r)/2
    XL = [z[0]-t/z[2] for z in XYC]
    XR = [z[0]+t/z[2] for z in XYC]
    YL = [z[1]-t/z[2] for z in XYC]
    YR = [z[1]+t/z[2] for z in XYC]
    if max(XL) <= min(XR) and max(YL) <= min(YR):
        r = t
    else:
        l = t

print(r)