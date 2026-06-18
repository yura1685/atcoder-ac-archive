from itertools import accumulate

N = int(input())
A = list(accumulate([0] + list(map(int, input().split()))))
M = int(input())
ans = 0
L = int(input()) - 1
for _ in range(M-1):
    B = int(input()) - 1
    ans += abs(A[B] - A[L])
    L = B
print(ans)