from itertools import accumulate

N, L, R = map(int, input().split())
A = [0] + list(map(int, input().split()))
S = list(accumulate(A))
B = [L*l - S[l] for l in range(N+1)]
C = [R*r + S[N-r] for r in range(N+1)]
M = C.copy()
for i in range(1, N+1):
    M[i] = min(M[i-1], C[i])

ans = 10 ** 18
for i in range(N+1):
    ans = min(ans, B[i] + M[N-i])

print(ans)