from collections import deque

N, K = map(int,input().split())
D = input().split()
XXX = '0123456789'
num = [i for i in XXX if i not in D]
d = deque(i for i in num)

while True:
    n = d.popleft()
    if int(n) >= N:
        exit(print(n))
    for m in num:
        d.append(n+m)

