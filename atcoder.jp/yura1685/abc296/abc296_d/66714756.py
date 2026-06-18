from math import isqrt
N, M = map(int,input().split())

ans = []
if N*N < M:
    print(-1)
    exit()
for a in range(1,N+1):
    if a >isqrt(M)+1:
        break
    b = (M+a-1)//a
    if 1 <= b <= N:
        ans.append(a*b)

print(min(ans))