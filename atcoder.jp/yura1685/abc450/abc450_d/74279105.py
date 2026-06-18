N, K = map(int, input().split())
A = sorted([int(a) % K for a in input().split()])
ans = A[-1] - A[0]
for i in range(N-1):
    ans = min(ans, A[i] + K - A[i+1])
print(ans)