s, t = input(), input()
n, m = len(s),  len(t)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j-1] + (s[i-1] == t[j-1]), dp[i-1][j], dp[i][j-1])

i, j = n, m
c = [(-1,0),(0,-1),(-1,-1)]
ans = []

while i + j:
    for di, dj in c:
        ni, nj = i + di, j + dj
        if dp[ni][nj] == dp[i][j]:
            i, j = ni, nj
            break
    else:
        ans.append(s[i-1])
        i, j = i-1, j-1

ans.reverse()
print(''.join(ans))