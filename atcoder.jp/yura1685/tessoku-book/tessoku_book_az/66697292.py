from collections import deque

Q = int(input())

retu = deque()
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        retu.append(q[1])
    elif q[0] == '2':
        print(retu[0])
    else:
        retu.popleft()
