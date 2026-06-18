N = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [[0]*10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(N-1):
    for j in range(10):
        X = dp[i][j]
        dp[i+1][(j+A[i+1])%10] += (X % mod)
        dp[i+1][(j*A[i+1])%10] += (X % mod)

for i in dp[-1]:
    print(i % mod)