from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]
D = defaultdict(int)
for i, a in enumerate(A):
    D[a] = max(D[a], i)
ans = [-1] * N
i = 0
while i < N:
    a = A[i]
    j = D[a]
    for k in range(i, j+1):
        ans[k] = a
    i = j + 1

print(*ans, sep='\n')