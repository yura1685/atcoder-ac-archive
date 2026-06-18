N, M = map(int,input().split())

cal = [list(map(int,input().split())) for _ in range(N)]

if all([cal[i+1][0] - cal[i][0] == 7 for i in range(N-1)]):
    for i in range(N):
        for j in range(M-1):
            if cal[i][j+1] - cal[i][j] != 1:
                print('No')
                exit()
    X = [cal[0][i] % 7 for i in range(M)]
    if 0 not in X or X[-1] == 0:
        print('Yes')
        exit()
print('No')