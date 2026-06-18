def Make_Line(A,B):
    ax, ay = A
    bx, by = B
    def f(x,y):
        return ((by-ay)*x + (ax-bx)*y + ay*bx - ax*by) == 0
    return f

def hoge(A,B):
    ax, ay = A
    bx, by = B
    return (by-ay, ax-bx, ay*bx-ax*by)


N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]

from random import randint

for _ in range(100):
    i = randint(0,N-1)
    while True:
        j = randint(0,N-1)
        if i != j:
            break
    f = Make_Line(P[i],P[j])
    cnt = 0
    for k in range(N):
        if f(P[k][0], P[k][1]):
            cnt += 1
    if (N+1)//2 <= cnt:
        print('Yes')
        print(*hoge(P[i],P[j]))
        exit()

print('No')