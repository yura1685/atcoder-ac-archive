N, K = map(int,input().split())
A = list(map(int,input().split()))

l, r = 1, sum(A)//K + 100
while r - l > 1:
    mid = (l+r)//2
    S = sum(min(a,mid) for a in A)
    if S >= K*mid:
        l = mid
    else:
        r = mid

print(l)