from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = deque()

for i in range(n):
    x = a[i]
    if i % 2 == 0:
        b.append(x)
    else:
        b.appendleft(x)

l = list(b)
if n % 2 == 0:
    print(*l)
else:
    l.reverse()
    print(*l)