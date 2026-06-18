from collections import defaultdict

N, W = map(int,input().split())
bag = [tuple(map(int,input().split())) for _ in range(N)]
case3 = True if 30 < N and max(bag[i][0] for i in range(N)) <= 1000 else False

if not case3:
    dp = defaultdict(int)
    dp[0] = 0
    for i in range(N):
        v, w = bag[i]
        now = list(dp.items())
        
        if w <= W:
            dp[w] = max(dp[w], v)

        for wei, val in now:
            if w + wei <= W:
                dp[w+wei] = max(dp[w+wei], v + val)
    
    print(max(dp.values()))

else:
    dp = defaultdict(lambda: float('inf'))
    dp[0] = 0
    for i in range(N):
        v, w = bag[i]
        now = list(dp.items())
        for val, wei in now:
            new_val = v + val
            new_wei = w + wei
            if new_wei <= W:
                if new_wei < dp[new_val]:
                    dp[new_val] = new_wei
    
    print(max(dp.keys()))