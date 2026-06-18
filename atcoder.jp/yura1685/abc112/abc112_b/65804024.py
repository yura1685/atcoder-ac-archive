N, T = map(int,input().split())
cost = 1685
for i in range(1,N+1):
    c, t = map(int,input().split())
    if t <= T:
        cost = min(cost, c)
print('TLE' if cost == 1685 else cost)