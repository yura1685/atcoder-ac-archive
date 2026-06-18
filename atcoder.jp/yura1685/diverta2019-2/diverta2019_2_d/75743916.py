N = int(input())
gA, sA, bA = map(int, input().split())
gB, sB, bB = map(int, input().split())

ops_AB = []
ops_BA = []
for cA, cB in [(gA, gB), (sA, sB), (bA, bB)]:
    if cB > cA:
        ops_AB.append((cB - cA, cA))
    if cA > cB:
        ops_BA.append((cA - cB, cB))

dp_A = [0] * (N + 1)
for k in range(1, N + 1):
    dp_A[k] = dp_A[k - 1]
    for p, c in ops_AB:
        if k >= c:
            dp_A[k] = max(dp_A[k], dp_A[k - c] + p)

max_P_AB = dp_A[N]
K_max = N + max_P_AB

dp_B = [0] * (K_max + 1)
for k in range(1, K_max + 1):
    dp_B[k] = dp_B[k - 1]
    for p, c in ops_BA:
        if k >= c:
            dp_B[k] = max(dp_B[k], dp_B[k - c] + p)

ans = N
for k in range(N + 1):
    K = N + dp_A[k]
    ans = max(ans, N + dp_A[k] + dp_B[K])

print(ans)