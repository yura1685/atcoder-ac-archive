from typing import List

def bit_count(n:int) -> int:
    res = 0
    for i in range(10):
        if (n >> i) & 1:
            res += 1
    return res

def solve():
    I = input().split()
    H, W = int(I[0]), int(I[1])
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
    
    inf = 10 ** 8
    dp:List[List[int]] = [[inf] * (1 << W) for _ in range(H)]
    for i in range(1 << W):
        if (i & S[0]) == i:
            dp[0][i] = bit_count(S[0]) - bit_count(i)
    
    for h in range(1,H):
        h_bitcnt = bit_count(S[h])
        for w in range(1 << W):
            if (w & S[h]) != w:
                continue

            n = h_bitcnt - bit_count(w)
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