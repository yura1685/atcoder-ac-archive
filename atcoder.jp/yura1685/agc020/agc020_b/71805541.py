K = map(int,input().split())
A = list(map(int,input().split()))
A = list(reversed(A))
if A[0] != 2: exit(print(-1))

m, M = 2, 2
for a in A:
    x, X = (m//a)*a, (M//a)*a
    if x < m: x += a
    if x > X: exit(print(-1))
    m, M = x, X + a - 1

print(m,M)