N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if A[i] + K < A[i-1]:
        ans += A[i-1] - K - A[i]
        A[i] = A[i-1] - K

for i in range(N-2,-1,-1):
    if A[i] + K < A[i+1]:
        ans += A[i+1] - K - A[i]
        A[i] = A[i+1] - K

print(ans)