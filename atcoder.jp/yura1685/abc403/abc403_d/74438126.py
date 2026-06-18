N, D = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)
C = [0] * (M+1)
for a in A: C[a] += 1

if D == 0:
    print(sum(c - 1 for c in C if c))
    exit()

ans = 0
for i in range(D):
    L = C[i::D]
    dp0, dp1 = 0, 0
    for cnt in L:
        dp0, dp1 = max(dp0, dp1), dp0 + cnt
    ans += max(dp0, dp1)

print(N - ans)