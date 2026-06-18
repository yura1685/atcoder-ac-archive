N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N//2):
    for j in range(i, N-1-i):
        if (i + 1) % 4 == 0:
            pass
        elif (i + 1) % 4 == 1:
            A[i][j], A[j][N-1-i], A[N-1-i][N-1-j], A[N-1-j][i] = A[N-1-j][i], A[i][j], A[j][N-1-i], A[N-1-i][N-1-j]
        elif (i + 1) % 4 == 2:
            A[i][j], A[j][N-1-i], A[N-1-i][N-1-j], A[N-1-j][i] = A[N-1-i][N-1-j], A[N-1-j][i], A[i][j], A[j][N-1-i]
        else:
            A[i][j], A[j][N-1-i], A[N-1-i][N-1-j], A[N-1-j][i] = A[j][N-1-i], A[N-1-i][N-1-j], A[N-1-j][i], A[i][j]

for a in A:
    print(''.join(a))