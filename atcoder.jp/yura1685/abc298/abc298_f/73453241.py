from collections import defaultdict

N = int(input())
sum_x = defaultdict(int)
sum_y = defaultdict(int)
d = defaultdict(int)
for _ in range(N):
    x, y, n = map(int,input().split())
    sum_x[x] += n 
    sum_y[y] += n 
    d[(x,y)] = n 

X = sorted([(s, x) for x, s in sum_x.items()], reverse=True)
Y = sorted([(s, y) for y, s in sum_y.items()], reverse=True)

ans = 0
for sx, x in X:
    if sx + Y[0][0] <= ans:
        break
    for sy, y in Y:
        if sx + sy <= ans:
            break
        ans = max(ans, sx + sy - d[(x,y)])

print(ans)