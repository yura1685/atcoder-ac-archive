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
while moveT or moveA:
    s, a = moveT.popleft()
    t, b = moveA.popleft()
    move = min(a,b)
    # print(s,t,move)
    # print(Tx,Ty,Ax,Ay)
    if s == t:
        if (Tx, Ty) == (Ax, Ay):
            ans += move
        Tx, Ty = f(Tx,Ty,s,move)
        Ax, Ay = f(Ax,Ay,t,move)
    elif (Tx,Ty) == (Ax,Ay):
        Tx, Ty = f(Tx,Ty,s,move)
        Ax, Ay = f(Ax,Ay,t,move)
    elif set([s,t]) == set(['U', 'D']):
        Tx2, Ty2 = f(Tx,Ty,s,move)
        Ax2, Ay2 = f(Ax,Ay,t,move)       
        if Ty == Ay and Tx != Ax:
            # print(abs(Tx-Ax),abs(Tx2-Ax2))
            if max(abs(Tx-Ax),abs(Tx2-Ax2)) <= 2*move and abs(Tx-Ax) % 2 == 0:
                ans += 1
        Tx, Ty = Tx2, Ty2
        Ax, Ay = Ax2, Ay2
    elif set([s,t]) == set(['R', 'L']):
        Tx2, Ty2 = f(Tx,Ty,s,move)
        Ax2, Ay2 = f(Ax,Ay,t,move)       
        if Tx == Ax and Ty != Ay:
            if max(abs(Ty-Ay),abs(Ty2-Ay2)) <= 2*move and abs(Ty-Ay) % 2 == 0:
                ans += 1
        Tx, Ty = Tx2, Ty2
        Ax, Ay = Ax2, Ay2     
    else:
        Tx2, Ty2 = f(Tx,Ty,s,move)
        Ax2, Ay2 = f(Ax,Ay,t,move)
        if s in 'RL':
            Px, Py = Tx, Ay
            if (Ty <= Py <= Ty2 or Ty2 <= Py <= Ty) and (Ax <= Px <= Ax2 or Ax2 <= Px <= Ax):
                if abs(Ty-Py) == abs(Ax-Px):
                    ans += 1
        else:
            Px, Py = Ax, Ty
            if (Ay <= Py <= Ay2 or Ay2 <= Py <= Ay) and (Tx <= Px <= Tx2 or Tx2 <= Px <= Tx):
                if abs(Ay-Py) == abs(Tx-Px):
                    ans += 1
        Tx, Ty = Tx2, Ty2
        Ax, Ay = Ax2, Ay2 
    a, b = a - move, b - move
    if a:
        moveT.appendleft((s,a))
    if b:
        moveA.appendleft((t,b))

print(ans)