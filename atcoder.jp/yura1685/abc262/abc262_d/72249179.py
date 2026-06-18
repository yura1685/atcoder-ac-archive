N = int(input())
A = list(map(int,input().split()))
mod = 998244353

ans = 0
for i in range(1,N+1):
    dp = [[[0]*i for _ in range(i+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for j in range(N):
        for k in range(i+1):
            for l in range(i):
                dp[j+1][k][l] += dp[j][k][l]
                if k != i:
                    dp[j+1][k+1][(l+A[j])%i] += dp[j][k][l]

    ans += dp[N][i][0]

print(ans % mod)