N, Q = map(int,input().split())
c = [0]*N
for i in range(Q):
    L, R, T = map(int,input().split())
    c[L-1:R] = [T]*(R-L+1)
print(*c,sep='\n')