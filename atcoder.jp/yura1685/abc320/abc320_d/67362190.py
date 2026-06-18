from collections import deque

N, M = map(int,input().split())

look = [[] for _ in range(N+1)] #look[A] = (B,X,Y). Aから見てBの座標
for _ in range(M):
    A, B, X, Y = map(int,input().split())
    look[A].append((B,X,Y))
    look[B].append((A,-X,-Y))

check = [0]*(N+1) # 人iは確定しているか？
check[1] = 1
d = deque([1])
xy = [(0,0) for _ in range(N+1)] # 人iの座標

while d:
    A = d.popleft()
    for B, X, Y in look[A]:
        if check[B] == 0:
            check[B] = 1
            xy[B] = (xy[A][0]+X,xy[A][1]+Y)
            d.append(B)

for i in range(1,N+1):
    if check[i]:
        print(*xy[i])
    else:
        print('undecidable')