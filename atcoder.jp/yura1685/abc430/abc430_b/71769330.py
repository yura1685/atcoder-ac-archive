N, M = map(int,input().split())
S = [input() for _ in range(N)]

s = set()
for i in range(N-M+1):
    for j in range(N-M+1):
        X = ""
        for k in range(M):
            X += S[i+k][j:j+M]
        s.add(X)

print(len(s))