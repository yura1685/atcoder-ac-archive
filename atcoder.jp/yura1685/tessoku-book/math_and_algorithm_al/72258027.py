from itertools import accumulate
T = int(input())
N = int(input())
C = [0] * T
for _ in range(N):
    l, r = map(int,input().split())
    C[l] += 1
    if r < T: C[r] -= 1
C = list(accumulate(C))
print(*C)