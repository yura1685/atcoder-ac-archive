W, H, x, y = map(int,input().split())

if (x,y) == (W/2,H/2):
    print(W*H/2, 1)
else:
    print(W*H/2, 0)