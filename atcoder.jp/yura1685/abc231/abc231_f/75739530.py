from collections import defaultdict
from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = N
d_a = defaultdict(int)
d_b = defaultdict(int)

for a in A:
    ans += d_a[a]
    d_a[a] += 1
for b in B:
    ans += d_b[b]
    d_b[b] += 1

AB = sorted((a, b) for a, b in zip(A, B))
S = SortedList()

for _, b in AB:
    idx = S.bisect_right(b)
    ans += len(S) - idx
    S.add(b)
    
print(ans)