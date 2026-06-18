from collections import deque

A, B, M = map(int,input().split())
a = deque(map(int,input().split()))
b = deque(map(int,input().split()))
a_min, b_min = min(a), min(b)
deque.appendleft(a,0)
deque.appendleft(b,0)

q_min = 10**10

for i in range(M):
    x,y,c = map(int,input().split())
    q_min = min(q_min, a[x]+b[y]-c)
print(min(a_min+b_min, q_min))
