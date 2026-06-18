H, W, N = map(int,input().split())
P = []
Hmax, Wmax = [-1] * H, [-1] * W
for i in range(N):
    h, w, a = map(int,input().split())
    P.append((a,i,h-1,w-1))

P.sort(reverse=True)

dp = [0] * N
pre = P[0][0]
L = []

for a, i, h, w in P:
    if a < pre:
        for ph, pw, ind in L:
            Hmax[ph] = max(Hmax[ph], dp[ind])
            Wmax[pw] = max(Wmax[pw], dp[ind])
        L.clear()
        pre = a
    dp[i] = max(Hmax[h], Wmax[w]) + 1
    L.append((h,w,i))

for a in dp:
    print(a)