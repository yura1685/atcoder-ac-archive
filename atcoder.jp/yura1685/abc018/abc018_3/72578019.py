H, W, K = map(int,input().split())
S = [input() for _ in range(H)]

U = [[0]*W for _ in range(H)]
D = [[0]*W for _ in range(H)]

for c in range(W):
    cnt1 = 0
    for r in range(H-1):
        if S[r][c] == 'o':
            cnt1 += 1
        else:
            cnt1 = 0
        U[r+1][c] = cnt1
    cnt2 = 0
    for r in range(H-1,0,-1):
        if S[r][c] == 'o':
            cnt2 += 1
        else:
            cnt2 = 0
        D[r-1][c] = cnt2

ans = 0
for h in range(K-1,H-K+1):
    for w_mid in range(K-1,W-K+1):
        if S[h][w_mid] == 'x':
            continue
        flag = True
        for w in range(w_mid-K+1,w_mid+K):
            if S[h][w] == 'x':
                flag = False
                break
            if U[h][w] < K - abs(w-w_mid) - 1 or D[h][w] < K - abs(w-w_mid) - 1:
                flag = False
                break
        if flag:
            ans += 1

print(ans)