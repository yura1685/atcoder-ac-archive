N, D = map(int, input().split())
W = list(map(int, input().split()))

total = 1 << N

weight = [0] * total
for S in range(total):
    for i in range(N):
        if S >> i & 1:
            weight[S] = weight[S ^ (1 << i)] + W[i]
            break

INF = float('inf')

dp = [INF] * (1 << N)
dp[0] = 0

for _ in range(D):
    dp2 = [INF] * (1 << N)
    for S in range(1 << N):
        if dp[S] == INF:
            continue
        nokori = ((1 << N) - 1) ^ S 
        T = nokori
        while T > 0:
            cost = weight[T] ** 2
            ns = S | T
            if dp[S] + cost < dp2[ns]:
                dp2[ns] = dp[S] + cost
            T = (T - 1) & nokori
        if dp[S] < dp2[S]:
            dp2[S] = dp[S]
    dp = dp2

sum_sq = dp[(1 << N) - 1]

total_w = sum(W)
print((sum_sq * D - total_w * total_w) / D ** 2)