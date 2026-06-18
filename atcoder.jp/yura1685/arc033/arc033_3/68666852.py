from sortedcontainers import SortedSet

ss = SortedSet()
Q = int(input())
for _ in range(Q):
    T, X = map(int,input().split())
    if T == 1:
        ss.add(X)
    else:
        c = ss.pop(X-1)
        print(c)