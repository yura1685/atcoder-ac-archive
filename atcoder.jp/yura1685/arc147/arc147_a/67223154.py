from collections import deque

N = int(input())
A = list(map(int,input().split()))
A.sort()
A = deque(A)

ans = 0
while True:
    AM = A.pop()
    if not A: print(ans); exit()
    Am = A.popleft()
    d = AM % Am
    A.appendleft(Am)
    if d: A.appendleft(d)
    ans += 1