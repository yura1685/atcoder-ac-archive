N, M = map(int, input().split())
A = list(map(int, input().split()))
P = [0] * M
now = 1
for i in range(M):
    P[i] = now
    if now == A[i]:
        now += 1
    elif now == A[i] + 1:
        now -= 1

D = list(range(N+1))
ans = [0] * M

for i in reversed(range(M)):
    ans[i] = D[P[i]]
    D[A[i]], D[A[i]+1] = D[A[i]+1], D[A[i]]

for x in ans:
    print(x)