line1 = input().split()
N, X, Y = int(line1[0]), int(line1[1]), int(line1[2])

dish = []
for _ in range(N):
    line = input().split()
    dish.append((int(line[0]), int(line[1])))

dp = [dict[int, int]() for _ in range(N+1)]
dp[0][0] = 0

max_k = 0
for a, b in dish:
    for k in range(max_k, -1, -1):
        for val, wei in dp[k].items():
            nex_a, nex_b = val + a, wei + b
            if nex_a <= X and nex_b <= Y:
                if nex_a not in dp[k+1] or nex_b < dp[k+1][nex_a]:
                    dp[k+1][nex_a] = nex_b
    if max_k < N-1:
        max_k += 1

ans = 0
for k in range(N, -1, -1):
    if len(dp[k]) > 0:
        ans = k
        break

print(min(N, ans+1))