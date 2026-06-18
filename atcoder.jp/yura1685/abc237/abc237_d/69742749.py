from collections import deque

N = int(input())
S = input()
d = deque([N])

for i in range(N-1,-1,-1):
    s = S[i]
    if s == 'L':
        d.append(i)
    else:
        d.appendleft(i)

print(*d)