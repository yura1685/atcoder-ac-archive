from itertools import accumulate

N, K = map(int, input().split())
A = [0] + list(accumulate(map(int, input().split())))
ans = 0
for i in range(N-K+1):
    if A[i+K] - A[i] <= 0:
        ans += 1
print(ans)