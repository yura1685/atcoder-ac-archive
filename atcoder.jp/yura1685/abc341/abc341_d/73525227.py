from math import lcm

N, M, K = map(int,input().split())
L = lcm(N,M)

l, r = 0, 10**20
while r - l > 1:
    mid = (l+r)//2
    if mid // N + mid // M - 2*(mid // L) >= K:
        r = mid
    else:
        l = mid

print(r)