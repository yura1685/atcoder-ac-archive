from itertools import product

N, M = map(int,input().split())
switch = [tuple(map(int,input().split())) for _ in range(M)]
p = list(map(int,input().split()))

c = list(product([0,1],repeat=N))
ans = 0
for T in c:
    on = 0
    for i in range(M):
        l = switch[i]
        cnt = 0
        for j in range(1,l[0]+1):
            if T[l[j]-1] == 1:
                cnt += 1
        if cnt % 2 == p[i]:
            on += 1
    if on == M:
        ans += 1

print(ans)