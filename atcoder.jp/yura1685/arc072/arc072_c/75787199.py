N, D = map(int, input().split())
d = list(map(int, input().split()))
Q = int(input())
q = list(map(int, input().split()))

A = [0] * N
A[0] = D
for i in range(1, N):
    A[i] = min(abs(A[i-1] - d[i-1]), A[i-1])

B = [sum(d)+1] * N + [1]
for i in range(N-1, -1, -1):
    if B[i+1] <= d[i] // 2:
        B[i] = B[i+1]
    else:
        B[i] = B[i+1] + d[i]

for i in range(Q):
    t = q[i]
    if A[t-1] >= B[t]:
        print('YES')
    else:
        print('NO')