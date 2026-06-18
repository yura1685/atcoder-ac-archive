N = int(input())
cnt = 0
hoge = 0
Q = []
for _ in range(N):
    x, y, z = map(int,input().split())
    cnt += z
    if x > y:
        hoge += z
    else:
        cost = (x+y)//2 + 1 - x
        Q.append((cost, z))

need = (cnt+1) // 2 - hoge

if need <= 0:
    exit(print(0))

dp = {0: 0}

for cost, seat in Q:
    items = list(dp.items())
    for s, cur_cost in items:
        ns = min(need, s+seat)
        new_cost = cur_cost + cost
        if new_cost < dp.get(ns, 10**18):
            dp[ns] = new_cost

print(dp[need])