from sortedcontainers import SortedList

sl = SortedList()

Q = int(input())
for _ in range(Q):
    n, x = map(int,input().split())
    if n == 1:
        sl.add(x)
    elif n == 2:
        sl.remove(x)
    else:
        i = sl.bisect_left(x)
        print(-1 if i == len(sl) else sl[i])