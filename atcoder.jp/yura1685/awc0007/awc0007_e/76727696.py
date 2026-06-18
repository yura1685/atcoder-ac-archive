N, M = map(int, input().split())

def dist(X, Y):
    h1, w1 = divmod(X-1, N)
    h2, w2 = divmod(Y-1, N)
    return abs(h1 - h2) + abs(w1 - w2)

S, T = map(int, input().split())
if M == 0: exit(print(dist(S, T)))
P = list(map(int, input().split()))

inf = 10 ** 18
dp = [[inf] * M for _ in range(1 << M)]
for i in range(M):
    dp[1 << i][i] = dist(S, P[i])
for mask in range(1, 1 << M):
    if mask.bit_count() == 1:
        continue
    for i in range(M):
        if (mask >> i) & 1:
            frm = mask ^ (1 << i)
            dp[mask][i] = min(dp[frm][j] + dist(P[j], P[i]) for j in range(M))

print(min(dp[(1 << M) - 1][i] + dist(P[i], T) for i in range(M)))