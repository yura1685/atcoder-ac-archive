N, _ = map(int,input().split())
A = set(map(int,input().split()))
M, m = max(A), min(A)

if M == N or m == 1:
    exit(print(-1))

ans = list(range(1,N+1))
for i in range(1,N-1):
    if i+1 in A:
        ans[i], ans[i+1] = ans[i+1], ans[i]

print(*ans)