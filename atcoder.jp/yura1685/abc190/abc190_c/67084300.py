from itertools import product

N, M = map(int,input().split())
check = [tuple(map(int,input().split())) for _ in range(M)]

K = int(input())
dish  = [tuple(map(int,input().split())) for _ in range(K)]

P = list(product((0,1),repeat=K))

ans = 0
for p in P:
    cnt = 0
    ball = [0]*(N+1)
    for i in range(K):
        ball[dish[i][p[i]]] += 1
    for c, d in check:
        if ball[c] > 0 and ball[d] > 0:
            cnt += 1
    ans = max(ans,cnt)

print(ans)