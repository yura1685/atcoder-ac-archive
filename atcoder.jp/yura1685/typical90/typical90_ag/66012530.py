H, W = map(int,input().split())
if H >= W:
    H, W = W, H

if H == 1:
    print(W)
    exit()
h, w = (H+1)//2, (W+1)//2
print(h*w)