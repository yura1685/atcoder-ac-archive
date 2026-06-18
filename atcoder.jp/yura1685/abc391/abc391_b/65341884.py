N, M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

hoge = 0
for a in range(N-M+1):
    for b in range(N-M+1):
        for m in range(M):
            for n in range(M):
                if S[a+m][b+n] == T[m][n]:
                    hoge += 1
        if hoge == M*M:
            print(a+1,b+1)
            exit()
        else:
            hoge = 0