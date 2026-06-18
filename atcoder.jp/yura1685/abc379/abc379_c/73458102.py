from collections import deque

def move(s, e, n):
    return (n-1)*n//2 - (n-e+s-1)*(n-e+s)//2

N, M = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))
if sum(A) != N or min(X) > 1: exit(print(-1))

d = deque(sorted((x, a) for x, a in zip(X,A)))
d.append((N+1,1))

ans = 0
while d:
    x, a = d.popleft()
    if x == N+1: break
    nex_x, nex_a = d.popleft()
    if x + a < nex_x:
        exit(print(-1))
    ans += move(x, nex_x, a)
    nex_a += a - (nex_x - x)
    d.appendleft((nex_x, nex_a))

print(ans)