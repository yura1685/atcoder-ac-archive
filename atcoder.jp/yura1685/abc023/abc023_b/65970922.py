from collections import deque

N = int(input())
S = input()

if N % 2 == 0:
    print(-1)
    exit()

d = deque(['b'])
for i in range(1,N//2+1):
    if i % 3 == 1:
        d.append('c')
        d.appendleft('a')
    elif i % 3 == 2:
        d.append('a')
        d.appendleft('c')
    else:
        d.append('b')
        d.appendleft('b')
d = list(d)
ac = ''.join(d)
if S == ac:
    print(N//2)
else:
    print(-1)