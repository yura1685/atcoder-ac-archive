from collections import deque

N, M = map(int,input().split())
C = [input() for _ in range(N)]

for n in range(N):
    for m in range(M):
        if C[n][m] == 's':
            si, sj = n, m 
        if C[n][m] == 'g':
            gi, gj = n, m 

pow = [1.0] * (N*M + 1)
for k in range(1, N*M+1):
    pow[k] = pow[k-1] * 0.99

move = [(-1,0),(0,-1),(0,1),(1,0)]
dp = [[-1]*M for _ in range(N)]
dq = deque([(si, sj, 0)])
dp[si][sj] = 10

while dq:
    i, j, t = dq.popleft()
    for di, dj in move:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            if C[ni][nj] == '#' or C[ni][nj] == 's':
                continue
            if C[ni][nj] == 'g':
                dp[ni][nj] = max(dp[ni][nj], dp[i][j])
            else:
                b = min(dp[i][j], int(C[ni][nj])*pow[t+1])
                if dp[ni][nj] < b:
                    dp[ni][nj] = b
                    dq.append((ni, nj, t+1))

ans = dp[gi][gj]
print(ans)