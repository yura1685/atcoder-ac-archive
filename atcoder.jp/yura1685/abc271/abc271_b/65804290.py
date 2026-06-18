from collections import deque
N, Q = map(int,input().split())
glid = []
for _ in range(N):
    x = deque(map(int,input().split()))
    x.popleft()
    glid.append(x)
for q in range(Q):
    s, t = map(int,input().split())
    print(glid[s-1][t-1])