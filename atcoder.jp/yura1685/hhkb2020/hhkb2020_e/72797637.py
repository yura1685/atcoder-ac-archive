H, W = map(int,input().split())
S = [input() for _ in range(H)]
Y = [[1]*W for _ in range(H)]
T = [[1]*W for _ in range(H)]

clear = H*W

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            Y[h][w] = T[h][w] = 0
            clear -= 1

for h in range(H):
    for w in range(1,W):
        if Y[h][w-1] == 0 or Y[h][w] == 0:
            continue
        Y[h][w] += Y[h][w-1]

for h in range(H):
    for w in range(W-2,-1,-1):
        if Y[h][w+1] == 0 or Y[h][w] == 0:
            continue
        Y[h][w] = Y[h][w+1]

for w in range(W):
    for h in range(1,H):
        if T[h-1][w] == 0 or T[h][w] == 0:
            continue
        T[h][w] += T[h-1][w]

for w in range(W):
    for h in range(H-2,-1,-1):
        if T[h+1][w] == 0 or T[h][w] == 0:
            continue
        T[h][w] = T[h+1][w]

mod = 10**9 + 7
n = 1
pow2 = [1]
for _ in range(H*W):
    n = n * 2 % mod
    pow2.append(n)

ans = 0
for h in range(H):
    for w in range(W):
        if Y[h][w] == 0:
            continue
        see = Y[h][w] + T[h][w] - 1
        ans += (pow2[clear] - pow2[clear - see]) % mod
        ans %= mod

print(ans)