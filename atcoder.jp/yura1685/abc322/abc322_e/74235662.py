N, K, P = map(int, input().split())
M = (P+1) ** K
inf = 10 ** 18
dp = [inf] * M
dp[0] = 0

for _ in range(N):
    C, *A = map(int, input().split())
    for s in range(M-1, -1, -1):
        if dp[s] == inf:
            continue
        psin = []
        cur_s = s
        for _ in range(K):
            psin.append(cur_s % (P+1))
            cur_s //= (P+1)
        psin.reverse()
        nex_s = 0
        for i in range(K):
            nex_v = min(P, psin[i] + A[i])
            nex_s = nex_s * (P+1) + nex_v
        if dp[nex_s] > dp[s] + C:
            dp[nex_s] = dp[s] + C

print(dp[-1] if dp[-1] < inf else -1)