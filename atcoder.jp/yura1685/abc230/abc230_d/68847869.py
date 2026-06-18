N, D = map(int,input().split())

M = []
for _ in range(N):
    L, R = map(int,input().split())
    M.append((R,L-1))
M.sort()

punch = 0
l, r = -1, -1
for R, L in M:
    if max(l,L) < min(r,R):
        pass
    else:
        l, r = R-1, R-1+D
        punch += 1

print(punch)