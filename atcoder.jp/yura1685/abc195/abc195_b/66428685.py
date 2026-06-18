A, B, W = map(int,input().split())
W *= 1000

M = W//A
m = (B+W-1)//B
if m <= M:
    print(m,M)
else:
    print('UNSATISFIABLE')