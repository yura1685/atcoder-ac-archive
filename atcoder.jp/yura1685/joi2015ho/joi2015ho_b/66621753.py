N = int(input())
cake = [int(input()) for _ in range(N)]

def solve(L):
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        if N % 2 == 1:
            dp[i][i] = L[i]
    for h in range(1,N):
        for w in range(N):
            i, j = w, (h+w) % N
            if i < j: n = j-i-1
            else:     n = N-i+j+1
            if (N-n) % 2 == 0:
                dp[i][j] = max(L[i]+dp[(i+1)%N][j], L[j]+dp[i][(j-1)%N])
            else:
                if L[i] > L[j]:
                    dp[i][j] = dp[(i+1)%N][j]
                else:
                    dp[i][j] = dp[i][(j-1)%N]
    return dp

ans = 0
for x in solve(cake):
    ans = max(ans,max(x))
print(ans)