H, W = map(int, input().split())
L = [['#']*W for _ in range(H)]
for i in range(1, H-1):
    for j in range(1, W-1):
        L[i][j] = '.'
for i in range(H):
    print(''.join(L[i]))