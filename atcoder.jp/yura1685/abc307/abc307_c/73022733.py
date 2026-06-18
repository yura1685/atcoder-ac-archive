HA, WA = map(int,input().split())
A_input = [input() for _ in range(HA)]
HB, WB = map(int,input().split())
B_input = [input() for _ in range(HB)]
HX, WX = map(int,input().split())
X_input = [input() for _ in range(HX)]
A, B, X = [], [], []

for i in range(HA):
    for j in range(WA):
        if A_input[i][j] == '#':
            A.append((i,j))
for i in range(HB):
    for j in range(WB):
        if B_input[i][j] == '#':
            B.append((i,j))
for i in range(HX):
    for j in range(WX):
        if X_input[i][j] == '#':
            X.append((i,j))

SX = set(X)
N = len(X)
a0, b0 = A[0], B[0]

for i in range(N):
    for j in range(N):
        xa, xb = X[i], X[j]
        dax, day = xa[0] - a0[0], xa[1] - a0[1]
        dbx, dby = xb[0] - b0[0], xb[1] - b0[1]
        C = set()
        for ax, ay in A:
            C.add((ax+dax, ay+day))
        for bx, by in B:
            C.add((bx+dbx, by+dby))
        if C == SX:
            exit(print('Yes'))

print('No')