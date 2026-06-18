from math import gcd

N, K = map(int,input().split())
if K == 1: exit(print('Infinity'))

P = []
for _ in range(N):
    X, Y = map(int,input().split())
    P.append((X,Y))

def line(P1,P2):
    x1, y1 = P1
    x2, y2 = P2
    res = [y2-y1, x1-x2, x2*y1 - x1*y2]
    return res

def on_line(a,b,c,P1):
    x, y = P1
    return a*x + b*y + c == 0

check = [[False]*N for _ in range(N)]
ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        if check[i][j]: continue
        a, b, c = line(P[i],P[j])
        s = [i,j]
        for k in range(j+1,N):
            if on_line(a,b,c,P[k]):
                s.append(k)
        if len(s) < K:
            continue
        for x in s:
            for y in s:
                check[x][y] = True
        ans += 1

print(ans)