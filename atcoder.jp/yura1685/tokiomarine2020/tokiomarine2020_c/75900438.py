from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    B = [0] * N
    for i in range(N):
        a = A[i]
        B[max(i-a, 0)] += 1
        if i+a+1 < N:
            B[i+a+1] -= 1
    A = list(accumulate(B))
    if A.count(N) == N:
        break

print(*A)