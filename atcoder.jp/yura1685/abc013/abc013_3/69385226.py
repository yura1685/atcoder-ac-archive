N, H = map(int,input().split())
A, B, C, D, E = map(int,input().split())

# 普通の食事をX (<=N)回するとする。
# このとき、食べた後の満腹度は H + X*B
# ここで、Y回質素な食事をしたとすると、満腹度は H + X*B + Y*D
# 残りの H-X-Y 日食事しなかったとき H+X*B+Y*D - (N-X-Y)*E > 0
# を満たす。これをYについて解くと、
# H - N*E + X*(B+E) + Y*(D+E) > 0
# Y*(D+E) > N*E - H - X*(B+E)
# Y > (N*E - H - X*(B+E)) / (D+E)
# を満たす最小のYを求める。

ans = 10**18
for X in range(N+1):
    up = N*E - H - X*(B+E)
    do = D + E
    if up % do == 0:
        Y = up // do + 1
    else:
        Y = (up + do - 1) // do
    Y = max(Y, 0)
    ans = min(ans, A*X + C*Y)

print(ans)