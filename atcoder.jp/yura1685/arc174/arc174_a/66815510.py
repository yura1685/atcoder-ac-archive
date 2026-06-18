N, C = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)

ans, s, m = 0, 0, 0
if C >= 1:
    for i in range(N):
        s += A[i]
        m = min(m, s)
        ans = max(ans, s-m)

elif C < 1:
    for i in range(N):
        s += A[i]
        m = max(m,s)
        ans = min(ans,s-m)


print(S+ans*(C-1))