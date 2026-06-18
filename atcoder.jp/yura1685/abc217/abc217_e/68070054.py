from sortedcontainers import SortedList
from collections import deque

Q = int(input())
A1 = SortedList()
A2 = deque()

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        A2.append(q[1])
    if q[0] == 2:
        if A1:
            u = A1.pop(0)
        else:
            u = A2.popleft()
        print(u)
    if q[0] == 3:
        for a in A2:
            A1.add(a)
        A2 = deque()

