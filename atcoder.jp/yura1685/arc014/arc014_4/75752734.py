from bisect import bisect_left
from itertools import accumulate

all, N, M = map(int, input().split())
L = [int(input()) for _ in range(N)]
D = sorted(L[i+1] - L[i] - 1 for i in range(N-1))
E = [0] + list(accumulate(D))

def solve():
    x, y = map(int, input().split())
    ans = N + min(L[0] - 1, x) + min(all - L[-1], y)
    z = x + y
    i = bisect_left(D, z)
    ans += E[i] + z * (N - 1 - i)
    print(ans)

for _ in range(M):
    solve()