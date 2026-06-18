N = int(input())
S = []
for _ in range(N):
  s = int(input())
  if s:
    S.append(s)
S.sort()

from bisect import bisect_left
def check(x, q):
  idx = bisect_left(S, x)
  a = len(S) - idx
  return a <= q

Q = int(input())
for _ in range(Q):
  q = int(input())
  ok = 10**6 + 1
  ng = -1
  while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid, q):
      ok = mid
    else:
      ng = mid
  print(ok)