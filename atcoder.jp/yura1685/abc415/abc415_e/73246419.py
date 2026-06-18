from collections import deque

H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
P = list(map(int,input().split()))
c = [(1,0), (0,1)]

def solve(n):
    coin = n + A[0][0] - P[0]
    dq = deque([(0,0,coin)])
    if coin < 0: return False
    dp = [[-1]*W for _ in range(H)]
    dp[0][0] = coin
    while dq:
        h, w, coin = dq.popleft()
        if coin < dp[h][w]: continue      
        for dh, dw in c:
            nh, nw = h+dh, w+dw
            if not (0 <= nh < H and 0 <= nw < W): continue
            coin2 = coin + A[nh][nw] - P[nh+nw]
            if coin2 < 0: continue
            if dp[nh][nw] < coin2:
                dp[nh][nw] = coin2
                dq.append((nh,nw,coin2))
    return True if dp[-1][-1] >= 0 else False

ng, ok = -1, 10**20
while ok - ng > 1:
    mid = (ng + ok) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)