N = int(input())
parts = []
S = 0
for _ in range(N):
    W, H, B = map(int,input().split())
    V = H - B
    S += W
    parts.append((W,H,B))

dp0 = [0]*S
dp1 = [0]*S
for i in range(N):
    w, h, b = parts[i]
    for j in range(min(S//2+1,S)):
        dp1[j] = dp0[j] + b
        if j - w >= 0:
            dp1[j] = max(dp1[j], dp0[j-w] + h)
    dp0 = dp1.copy()
    dp1 = [0]*S

print(dp0[S//2])