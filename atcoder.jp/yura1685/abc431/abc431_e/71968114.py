from collections import deque

dh = [1,0,-1,0]
dw = [0,1,0,-1]
dic = {'A':0, 'B':1, 'C':3}
 
def solve():
    H, W = map(int,input().split())
    S = [input() for _ in range(H)]
    inf = float('inf')
    dp = [[[inf]*4 for _ in range(W)] for _ in range(H)]
    # dp[h][w][d]: マス(h,w)から方向dに出るときの最小値
    dq = deque()
    dq.append((0,-1,0,1)) # (h,w,step,d)
    while dq:
        h, w, step, d = dq.popleft()
        h2, w2 = h + dh[d], w + dw[d]
        if not (0 <= h2 < H and 0 <= w2 < W): continue
        for nex in range(4):
            if d ^ nex == 2: continue
            if d ^ nex == dic[S[h2][w2]]:
                if step < dp[h2][w2][nex]:
                    dp[h2][w2][nex] = step
                    dq.appendleft((h2,w2,step,nex))
            else:
                if step + 1 < dp[h2][w2][nex]:
                    dp[h2][w2][nex] = step + 1
                    dq.append((h2,w2,step+1,nex))
    
    print(dp[H-1][W-1][1])

T = int(input())
for _ in range(T):
    solve()