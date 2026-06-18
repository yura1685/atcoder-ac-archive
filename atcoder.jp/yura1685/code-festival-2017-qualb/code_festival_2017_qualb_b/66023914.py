import bisect
from collections import Counter

N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

P = Counter(D)
T.sort()
X = set(T)

for k in X:
    num = P[k]
    if bisect.bisect_right(T, k) - bisect.bisect_left(T,k) > num:
        print('NO')
        exit()

print('YES')