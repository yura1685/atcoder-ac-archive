N = int(input())
A = list(map(int,input().split()))

dp = [0]*N
dp[0], dp[1] = A[0], A[1]
if N >= 3:
    dp[2] = A[2]+A[0]
for i in range(3,N):
    dp[i] = max(dp[i-2] + A[i],dp[i-3] + A[i])

print(max(dp[-1],dp[-2]))