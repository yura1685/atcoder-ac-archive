from sortedcontainers import SortedList

L, Q = map(int,input().split())
S = SortedList([0,L])

for _ in range(Q):
    c, x = map(int,input().split())
    if c == 1:
        S.add(x)
        continue
    n = S.bisect(x)
    print(S[n] - S[n-1])