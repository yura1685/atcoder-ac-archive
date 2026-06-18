X, Y, Z = map(int,input().split())
S = input()
dp = [[0]*len(S) for _ in range(2)]
dp[0][0] = X if S[0] == 'a' else Y
dp[1][0] = X + Z if S[0] == 'A' else Y + Z

for i in range(1,len(S)):
    if S[i] == 'a':
        dp[0][i] = min(dp[0][i-1] + X, dp[1][i-1] + Z + X)
        dp[1][i] = min(dp[1][i-1] + Y, dp[0][i-1] + Z + Y)
    if S[i] == 'A':
        dp[0][i] = min(dp[0][i-1] + Y, dp[1][i-1] + Z + Y)
        dp[1][i] = min(dp[1][i-1] + X, dp[0][i-1] + Z + X)

print(min(dp[0][-1], dp[1][-1]))