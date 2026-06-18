from itertools import accumulate

N, Q = map(int,input().split())
c = [0]*(N+1)
for _ in range(Q):
    l, r = map(int,input().split())
    c[l-1] += 1
    c[r] -= 1
c = list(accumulate(c))

ans = ''
for i in range(N):
    if c[i] % 2 == 0:
        ans += '0'
    else:
        ans += '1'

print(ans)