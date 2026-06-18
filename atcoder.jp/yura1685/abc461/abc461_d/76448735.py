from bisect import bisect_left, bisect_right

I = input().split()
H, W, K = int(I[0]), int(I[1]), int(I[2])
S = [[0] * (W+1) for _ in range(H+1)]
S_in = [input() for _ in range(H)]
for h in range(H):
    for w in range(W):
        if S_in[h][w] == '1':
            S[h+1][w+1] = 1

for h in range(1, H+1):
    for w in range(1, W+1):
        S[h][w] = int(S_in[h-1][w-1]) + S[h-1][w] + S[h][w-1] - S[h-1][w-1]

ans = 0
for h1 in range(1, H+1):
    for h2 in range(h1, H+1):
        now = [0] * (W + 1)
        for w in range(1, W+1):
            now[w] = S[h2][w] - S[h1-1][w]
        
        for w1 in range(1, W+1):
            l = now[w1-1] + K
            ind1 = bisect_left(now, l, w1, W+1)
            ind2 = bisect_right(now, l, w1, W+1)
            ans += (ind2 - ind1)

print(ans)