N, K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

def f(X):
    res = 0
    for i in range(N):
        a, f = A[i], F[i]
        res += max(0,(a*f-X+f-1)//f)
    return res <= K

l, r = -1, 10**12 + 1
while r - l > 1:
    mid = (l+r)//2
    if f(mid):
        r = mid
    else:
        l = mid

print(r)