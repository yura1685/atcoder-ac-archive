from collections import defaultdict
from bisect import bisect

W, H = map(int,input().split())
N = int(input())
st = [tuple(map(int,input().split())) for _ in range(N)]
a = int(input())
A = [0] + list(map(int,input().split())) + [W]
b = int(input())
B = [0] + list(map(int,input().split())) + [H]
d = defaultdict(int)

for p, q in st:
    i = bisect(A, p)
    j = bisect(B, q)
    d[(i,j)] += 1

m = 0 if len(d) < (a+1) * (b+1) else min(d.values())
M = max(d.values())

print(m, M)