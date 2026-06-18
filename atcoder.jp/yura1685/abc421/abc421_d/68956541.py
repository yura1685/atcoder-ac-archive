from collections import deque

Tx, Ty, Ax, Ay = map(int,input().split())
N, M, L = map(int,input().split())

moveT, moveA = deque(), deque()
for _ in range(M):
    S, A = input().split()
    moveT.append((S,int(A)))
for _ in range(L):
    T, B = input().split()
    moveA.append((T,int(B)))

def f(x,y,z,w): # (x,y) が方向 z に w 移動したときの座標
    if z == 'U': x -= w
    if z == 'D': x += w
    if z == 'R': y += w
    if z == 'L': y -= w
    return (x,y)

ans = 0
while moveT:
    s, a = moveT.popleft()
    t, b = moveA.popleft()
    move = min(a,b)
    D = abs(Tx-Ax) + abs(Ty-Ay)
    if (Tx,Ty) == (Ax,Ay):
        if  s == t:
            ans += move
    elif D % 2 == 1 or 2*move < D:
        pass
    else:
        Txm, Tym = f(Tx,Ty,s,D//2)
        Axm, Aym = f(Ax,Ay,t,D//2)
        if (Txm,Tym) == (Axm,Aym):
            ans += 1
    Tx, Ty = f(Tx,Ty,s,move)
    Ax, Ay = f(Ax,Ay,t,move)
    a, b = a - move, b - move
    if a:
        moveT.appendleft((s,a))
    if b:
        moveA.appendleft((t,b))

print(ans)