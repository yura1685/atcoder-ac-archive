N = int(input())
A = [list(input()) for _ in range(N)]
B = [['']*N for _ in range(N)]

for h in range(N):
    for w in range(N):
        if h == 0 and w != N-1:
            B[h][w+1] = A[h][w]
        elif w == N-1 and h != N-1:
            B[h+1][w] = A[h][w]
        elif h == N-1 and w != 0:
            B[h][w-1] = A[h][w]
        elif w == 0 and h != 0:
            B[h-1][w] = A[h][w]
        else:
            B[h][w] = A[h][w]

for i in B:
    print(''.join(i))