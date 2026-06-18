N, R = map(int,input().split())
L = list(map(int,input().split()))
l, r = -1, -1
if R > 0:
    for i in range(R-1,-1,-1):
        if L[i] == 0:
            l = i

if R < N:
    for i in range(R,N):
        if L[i] == 0:
            r = i

cnt = 0
if l >= 0:
    for i in range(l,R):
        cnt += 1 + L[i]

if r >= 0:
    for i in range(R,r+1):
        cnt += 1 + L[i]

print(cnt)