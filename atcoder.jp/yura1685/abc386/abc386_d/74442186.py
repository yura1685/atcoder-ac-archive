N, M = map(int, input().split())
xyc = []
for _ in range(M):
    I = input().split()
    X, Y, C = int(I[0]), int(I[1]), I[2]
    xyc.append([X, Y, C])
xyc.sort()
W = N + 1
for x, y, c in xyc:
    if c == 'W':
        W = min(W, y)
    else:
        if W <= y:
            exit(print('No'))
print('Yes')