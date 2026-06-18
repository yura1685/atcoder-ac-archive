from collections import deque

d = deque([1,2,3,4,5,6,7,8,9])
K = int(input())
for _ in range(K):
    x = d.popleft()
    if x % 10 != 0:
        d.append(10*x + (x % 10) - 1)
    d.append(10*x + (x % 10))
    if x % 10 != 9:
        d.append(10*x + (x % 10) + 1)

print(x)