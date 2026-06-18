# 30 30 30
#    40 40
#       25 25 25 25
#                10
# __ __ __ __ __ __

# xx oo oo oo oo oo -> 40 + 25 + 10 = 75
# oo xx oo oo oo oo -> 25 + 10      = 35
# oo oo xx oo oo oo -> 10           = 10
# oo oo oo xx oo oo -> 30 + 40 + 10 = 80
# oo oo oo oo xx oo -> 30 + 40 + 10 = 80
# oo oo oo oo oo xx -> 30 + 40      = 70

# 30 + 40 + 25 + 10 = 105
# であるから、ある1点での総和を最小化する。

# 30 30 30
#    40 40
#       25 25 25 25
#  +             10
# -----------------
# 30 70 95 25 25 35
# ↑最小値は25. よって最大値は 105 - 25 = 80

# --------------------------------------------------------------

from itertools import accumulate
N, M = map(int,input().split())
A = [0] * (M+1)
S = 0
for _ in range(N):
    l, r, s = map(int,input().split())
    A[l-1] += s
    A[r] -= s
    S += s
AC = list(accumulate(A))

print(S - min(AC[:-1]))