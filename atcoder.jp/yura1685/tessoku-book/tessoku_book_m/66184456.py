import bisect

N, K = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    a = A[i]
    n = bisect.bisect(A,a+K)
    ans += n-i-1

print(ans)