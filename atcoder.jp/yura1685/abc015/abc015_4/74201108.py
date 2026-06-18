W = int(input())
N, K = map(int, input().split())
inf = 1 << 20
dp = [[inf] * (K+1) for _ in range(5001)]
dp[0][0] = 0

for i in range(N):
    w, v = map(int, input().split())
    for cur_v in range(5000, v-1, -1):
        for k in range(K, 0, -1):
            if dp[cur_v-v][k-1] + w <= W:
                dp[cur_v][k] = min(dp[cur_v][k], dp[cur_v-v][k-1] + w)

for v in range(5000, -1, -1):
    for k in range(K+1):
        if dp[v][k] <= W:
            exit(print(v))