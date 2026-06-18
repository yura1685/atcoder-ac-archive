N, P, Q = map(int, input().split())
PY, QY = 10 ** 18, 10 ** 18
d = {}
for _ in range(N):
    X, C = map(int, input().split())
    d[X] = C
    if abs(P - X) < abs(P - PY):
        PY = X
    elif abs(P - X) == abs(P - PY):
        PY = min(PY, X)
    if abs(Q - X) < abs(Q - QY):
        QY = X
    elif abs(Q - X) == abs(Q - QY):
        QY = min(QY, X)

if PY == QY:
    print(d[PY] + 2)
else:
    print(d[PY] + d[QY] + 2)