W, B = map(int,input().split())
W *= 1000
print(W//B+1 if W % B == 0 else (W+B-1)//B)