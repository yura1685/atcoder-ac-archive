T = input()
N = int(input())
INF = float('inf')
word = [input().split() for _ in range(N)]

dp = [[INF]*(len(T)+1) for _ in range(N+1)] 
# dp[i][j]: 袋iまででj文字目を作るときのコストの最小値
dp[0][0] = 0

for i in range(N):
    for j in range(len(T)+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        for s in word[i][1:]:
            if T[j:j+len(s)] == s:
                dp[i+1][j+len(s)] = min(dp[i+1][j+len(s)], dp[i][j]+1)

ans = dp[-1][-1]

print(ans if ans != INF else -1)