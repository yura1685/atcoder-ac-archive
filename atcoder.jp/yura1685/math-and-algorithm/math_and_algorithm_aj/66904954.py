from itertools import accumulate
N, Q = map(int,input().split())
snow = [0]*(N+1)
for _ in range(Q):
    L, R, X = map(int,input().split())
    snow[L-1] += X
    snow[R] -= X

c = list(accumulate(snow))

ans = ''
for i in range(N-1):
    if c[i] > c[i+1]:
        ans += '>'
    elif c[i] == c[i+1]:
        ans += '='
    else:
        ans += '<'

print(ans)