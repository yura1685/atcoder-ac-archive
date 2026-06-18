N = int(input())

HM, Hm = 0, 10**10
WM, Wm = 0, 10**10

s = set()

for _ in range(N):
    h, w = map(int,input().split())
    HM = max(HM,h)
    Hm = min(Hm,h)
    WM = max(WM,w)
    Wm = min(Wm,w)

print(max((HM-Hm+1)//2,(WM-Wm+1)//2))