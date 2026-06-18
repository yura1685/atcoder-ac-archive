from typing import List

def solve():
    H, W = map(int,input().split())
    S:List[int] = []
    for _ in range(H):
        X = input()
        n = 0
        for x in X:
            if x == '#':
                n = 2*n + 1
            else:
                n *= 2
        S.append(n)
    
    inf = float('inf')
    # dp[i][j]: i行目が状態jで、i行目まで条件を満たすときのコストの最小値
    dp = [[inf] * (1 << W) for _ in range(H)]
    for i in range(1 << W):
        if (i & S[0]) == i:
            dp[0][i] = S[0].bit_count() - i.bit_count()
    
    for h in range(1,H):
        for w in range(1 << W):
            if (w & S[h]) != w:
                continue

            n = S[h].bit_count() - w.bit_count()
            m = inf
            for w2 in range(1 << W):
                if dp[h-1][w2] == inf:
                    continue

                for bit in range(W-1):
                    if (w >> bit) & 1 and (w >> bit+1) & 1 and \
                       (w2 >> bit) & 1 and (w2 >> bit+1) & 1:
                        break
                else:
                    m = min(m, n+dp[h-1][w2])
            dp[h][w] = m
    print(min(dp[-1]))

for _ in range(int(input())):
    solve()