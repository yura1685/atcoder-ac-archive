import bisect
from itertools import accumulate

N, M = map(int,input().split())
H = sorted(map(int,input().split()))
W = list(map(int,input().split()))

H1 = [0] + [H[i+1]-H[i] for i in range(0,N-1,2)]
H2 = [0] + [H[i+1]-H[i] for i in range(1,N-1,2)]
H1AC = list(accumulate(H1))
H2AC = list(accumulate(H2))

ans = 10**10
for w in W:
    l = bisect.bisect_left(H, w)
    r = bisect.bisect_right(H,w)
    if l % 2 == 1: l -= 1
    ans = min(ans, H1AC[l//2] + abs(w-H[l]) + H2AC[-1] - H2AC[l//2])
    if r % 2 == 1: r -= 1
    ans = min(ans, H1AC[r//2] + abs(w-H[r]) + H2AC[-1] - H2AC[r//2])

print(ans)