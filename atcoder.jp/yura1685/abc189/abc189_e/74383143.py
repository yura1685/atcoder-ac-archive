#ABC189(E) Rotate and Flip

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

Loc = [[(0,0), (1,0), (0,1)]]
M = int(input())
for _ in range(M):
    q = input().split()
    O, ex, ey = Loc[-1]
    if q[0] == '1':
        O = (O[1], -O[0])
        ex = (ex[1], -ex[0])
        ey = (ey[1], -ey[0])
    elif q[0] == '2':
        O = (-O[1], O[0])
        ex = (-ex[1], ex[0])
        ey = (-ey[1], ey[0])
    elif q[0] == '3':
        p = int(q[1])
        O = (2*p - O[0], O[1])
        ex = (2*p - ex[0], ex[1])
        ey = (2*p - ey[0], ey[1])
    elif q[0] == '4':
        p = int(q[1])
        O = (O[0], 2*p - O[1])
        ex = (ex[0], 2*p - ex[1])
        ey = (ey[0], 2*p - ey[1])
    Loc.append([O, ex, ey])

Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    O, ex, ey = Loc[A]
    x, y = P[B-1]
    vx = (ex[0] - O[0], ex[1] - O[1])
    vy = (ey[0] - O[0], ey[1] - O[1])
    ansx = O[0] + x * vx[0] + y * vy[0]
    ansy = O[1] + x * vx[1] + y * vy[1]
    print(ansx, ansy)