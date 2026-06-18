Q = int(input())
A, B = [], []
a = 0

for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        A.append(x)
        a += 1
    elif t == 2:
        B.append(x)
    else:
        if x <= a:
            print(A[-x])
        else:
            x -= a
            print(B[x-1])