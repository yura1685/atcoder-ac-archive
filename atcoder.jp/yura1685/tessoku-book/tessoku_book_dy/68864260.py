from collections import deque

N, X = map(int,input().split())
A = list(input())
d = deque()
d.append(X-1)
A[X-1] = '@'
while d:
    u = d.popleft()
    if u > 0 and A[u-1] == '.':
        A[u-1] = '@'
        d.append(u-1)
    if u < N-1 and A[u+1] == '.':
        A[u+1] = '@'
        d.append(u+1)

print(''.join(A))