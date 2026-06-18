W, H, Q = map(int, input().split())
inf = float('inf')
Tate = []
Yoko = []
for _ in range(Q):
    T, D, X = map(int, input().split())
    if D == 0:
        Tate.append((T, X-1))
    else:
        Yoko.append((T, X-1))
Tate.sort(reverse=True)
Yoko.sort(reverse=True)

def solve(N, Beam):
    dp = [0] * N
    while Beam:
        now = Beam[-1][0]
        pos = []
        while Beam and Beam[-1][0] == now:
            pos.append(Beam.pop()[1])
        i = 0
        m = len(pos)
        while i < m:
            j = i
            while j + 1 < m and pos[j+1] == pos[j] + 1:
                j += 1
            L, R = pos[i], pos[j]
            left = dp[L-1] if L > 0 else inf
            right = dp[R+1] if R < N - 1 else inf
            for k in range(L, R+1):
                dp[k] = min(left+k-L+1, right+R-k+1)
            i = j + 1
    return min(dp)

ans = solve(W, Tate) + solve(H, Yoko)
print(ans if ans < inf else -1)