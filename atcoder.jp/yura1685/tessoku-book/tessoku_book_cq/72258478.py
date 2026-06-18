N, S = map(int,input().split())
A = [0] + list(map(int,input().split()))
# dp[i][j]: i番目までで、総和がjとなるように選べるか？
dp = [[False]*(S+1) for _ in range(N+1)]
for i in range(N+1): dp[i][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[i][j] == False: continue
        dp[i+1][j] = True
        if j + A[i+1] <= S:
            dp[i+1][j+A[i+1]] = True

if not dp[-1][-1]: exit(print(-1))

ans = []
j = S
for i in range(N,-1,-1):
    if dp[i-1][j]: continue
    ans.append(i)
    j -= A[i]
ans.reverse()

print(len(ans))
print(*ans)