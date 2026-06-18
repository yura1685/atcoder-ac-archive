N = int(input())
S = [list(input()) for _ in range(N)]
for k in range(2*N-1):
    X = [0] * 11
    for i in range(N):
        j = k - i
        if 0 <= j < N:
            if S[i][j] == '?':
                X[10] += 1
            else:
                X[int(S[i][j])] += 1
    if X[:10].count(0) < 9:
        exit(print(-1))
    for n in range(10):
        if X[n] == 0:
            continue
        m = str(n)
        for i in range(N):
            j = k - i
            if 0 <= j < N:
                S[i][j] = m
        break
    else:
        for i in range(N):
            j = k - i
            if 0 <= j < N:
                S[i][j] = '0'

for s in S: print(''.join(s))