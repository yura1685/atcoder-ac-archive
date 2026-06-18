H, W = map(int,input().split())
if H == 1 or W == 1:
    print(1);exit()
elif H % 2 == 0:
    print(H*W//2);exit()
elif W % 2 == 0:
    print(H*W//2);exit()
else:
    print(W*(H//2)+W//2+1)