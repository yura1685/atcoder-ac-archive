N, M = map(int, input().split())
L, R, *A = map(int, input().split())
A.sort()
ans = 1 << 60

for i in range(N-M-1):
    l, r = A[i], A[i+M-1]
    ans = min(ans, max(L-l, 0) + max(r-R, 0))

print(ans)