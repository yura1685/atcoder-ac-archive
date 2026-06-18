N = int(input())
S = input()
atc = 'atcoder'
mod = 10**9+7
dp = [[1]*(N+1)]+[[0]*(N+1) for _ in range(7)]

for h in range(1,8):
    for w in range(1,N+1):
        if atc[h-1] == S[w-1]:
            dp[h][w] = (dp[h-1][w] + dp[h][w-1]) % mod
        else:
            dp[h][w] = dp[h][w-1]

print(dp[-1][-1])