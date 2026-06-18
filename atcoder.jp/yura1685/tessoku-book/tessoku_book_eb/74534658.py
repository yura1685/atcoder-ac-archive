from sortedcontainers import SortedSet

inf = 10 ** 18
S = SortedSet([-inf, inf])
flag = False

Q = int(input())
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        S.add(x)
        flag = True
    else:
        if not flag:
            print(-1)
        else:
            idx = S.bisect(x)
            print(min(x-S[idx-1], S[idx]-x))