from itertools import product

N = int(input())
Ma = []

for _ in range(N):
    A = int(input())
    X, Y = [], []
    for __ in range(A):
        x, y = map(int,input().split())
        if y == 0:
            Y.append(x-1)
        else:
            X.append(x-1)
    Ma.append([X,Y])

perm = list(product((0,1),repeat=N))
ans = 0
for p in perm:
    hoge = 0
    for i in range(N):
        if p[i] == 0:
            continue
        if all([p[a] == 1 for a in Ma[i][0]]) and all([p[a] == 0 for a in Ma[i][1]]):
            pass
        else:
            break
    else:
        ans = max(ans,sum(p))
print(ans)