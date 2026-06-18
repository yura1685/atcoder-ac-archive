H, W = map(int,input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0); exit()

ans = min(H,W)

for h in range(1,H):
    A = h*W
    B = W//2*(H-h)
    C = (W+1)//2*(H-h)
    ans = min(ans,max(A,B,C)-min(A,B,C))

for w in range(1,W):
    A = H*w
    B = H//2*(W-w)
    C = (H+1)//2*(W-w)
    ans = min(ans,max(A,B,C)-min(A,B,C))

print(ans)