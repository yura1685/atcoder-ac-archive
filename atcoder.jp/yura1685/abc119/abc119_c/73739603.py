from itertools import product

N, A, B, C = map(int,input().split())
L = [int(input()) for _ in range(N)]

ans = 16851685
for P in product([0,1,2,3], repeat=N):
    a, b, c = [], [], []
    for i in range(N):
        if P[i] == 0:
            a.append(L[i])
        if P[i] == 1:
            b.append(L[i])
        if P[i] == 2:
            c.append(L[i])
    if not (a and b and c):
        continue
    hoge = 0
    hoge += 10*(len(a)-1) + abs(sum(a) - A)
    hoge += 10*(len(b)-1) + abs(sum(b) - B)
    hoge += 10*(len(c)-1) + abs(sum(c) - C)
    ans = min(hoge, ans)

print(ans)