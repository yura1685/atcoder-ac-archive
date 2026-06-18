from collections import deque
from sortedcontainers import SortedList

N, K = map(int,input().split())
d = deque()
sl = SortedList() # 店の中にいる人の (退店時間, 人数)
man = 0 # 現在店の中にいる人の数
time = 0 # 現在時刻

for i in range(N):
    A, B, C = map(int,input().split())
    if A < time:
        A = time
    while sl and sl[0][0] <= A:
        _, out = sl.pop(0)
        man -= out
    while man + C > K:
        A, out = sl.pop(0)
        man -= out
    time = A
    sl.add((A+B,C))
    man += C
    print(A)