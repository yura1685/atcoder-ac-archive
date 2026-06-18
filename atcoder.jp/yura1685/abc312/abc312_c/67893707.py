from bisect import *

N, M = map(int,input().split())
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))

l, r = 0, 10**9+1
while r - l > 1:
    mid = (l+r)//2
    if bisect(A,mid) >= M - bisect_left(B,mid):
        r = mid
    else:
        l = mid

print(r)