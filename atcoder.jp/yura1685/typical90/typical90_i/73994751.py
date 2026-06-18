from math import pi, atan2
from bisect import bisect_left

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
pi2 = 2 * pi

ans = 0
for j in range(N):
    xj, yj = P[j]
    A = []
    for n in range(N):
        if n == j:
            continue
        xn, yn = P[n]
        angle = atan2(yn - yj, xn - xj) % pi2
        A.append(angle)
    A.sort()
    A = A + [a + pi2 for a in A]

    for n in range(N-1):
        i = A[n]
        k = bisect_left(A, i + pi)
        diff1 = A[k-1] - i
        if diff1 > pi: diff1 = pi2 - diff1
        ans = max(ans, diff1)
        if k < len(A):
            diff2 = A[k] - i
            if diff2 > pi:
                diff2 = pi2 - diff2
            ans = max(ans, diff2)

print(ans * 180 / pi)