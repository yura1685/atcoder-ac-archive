N, Q = map(int,input().split())
d = {}

for _ in range(Q):
    T, A, B = map(int,input().split())
    if T == 1:
        d[(A,B)] = 1
    elif T == 2:
        d[(A,B)] = 0
    else:
        if d.get((A, B)) == 1 and d.get((B, A)) == 1:
            print('Yes')
        else:
            print('No')