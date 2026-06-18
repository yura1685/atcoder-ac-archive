from bisect import bisect_left
from itertools import accumulate

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = [0] + list(accumulate(A))

def f(X):
    res = 0
    for a in A:
        res += N - bisect_left(A, X-a)
    return res

ng, ok = 0, 10 ** 12
while ok - ng > 1:
    mid = (ng + ok) // 2
    if M < f(mid):
        ng = mid
    else:
        ok = mid

ans = 0
for a in A:
    i = bisect_left(A, ok-a)
    ans += (N - i) * a + B[N] - B[i]
    M -= (N-i)

print(ans + M * ng)