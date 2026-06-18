H, W = map(int,input().split())
S = [input() for _ in range(H)]

T = [[] for _ in range(H+W-1)]
for h in range(H):
    for w in range(W):
        s = S[h][w]
        T[h+w].append(s)

cnt = 0
for l in T:
    if 'B' in l:
        if 'R' in l:
            exit(print(0))
        pass
    elif 'R' in l:
        pass
    else:
        cnt += 1

print(pow(2,cnt,998244353))