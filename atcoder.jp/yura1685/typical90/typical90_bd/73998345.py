N, S = map(int, input().split())
# dp[i][j]: i日目までにj円分買うことは可能か？
dp = [[""] * (S+1) for _ in range(N+1)]
dp[0][0] = ' '
Q = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    A, B = Q[i]
    for j in range(S+1):
        if not dp[i][j]:
            continue
        if j + A <= S:
            dp[i+1][j+A] = 'A'
        if j + B <= S:
            dp[i+1][j+B] = 'B'

if not dp[N][S]:
    exit(print('Impossible'))

ans = []
now = S
for i in range(N):
    if dp[N-i][now] == 'A':
        ans.append('A')
        now -= Q[N-1-i][0]
    else:
        ans.append('B')
        now -= Q[N-1-i][1]

ans.reverse()
print(''.join(ans))