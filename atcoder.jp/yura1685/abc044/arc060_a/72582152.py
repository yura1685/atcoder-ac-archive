from collections import defaultdict

N, A = map(int,input().split())
X = list(map(int,input().split()))

dp = [defaultdict(int) for _ in range(N+1)]
dp[0][0] = 1

for x in X:
    for j in range(N,0,-1):
        for s, cnt in dp[j-1].items():
            dp[j][s+x] += cnt

ans = 0
for j in range(1,N+1):
    ans += dp[j][j*A]

print(ans)