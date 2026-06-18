import bisect

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    if A[i] > A[-1]:
        break
    num = 2*A[i] - 1
    ans += N - bisect.bisect(A,num)

print(ans)