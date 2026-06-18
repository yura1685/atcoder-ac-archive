from itertools import product
H, W, K = map(int,input().split())
choco = [input() for _ in range(H)]

ans = 10**8
for cut in product([0,1], repeat=H-1):
    S = sum(cut)
    cnt = S
    A = []
    X = [choco[0]]
    for i in range(H-1):
        if cut[i] == 0:
            X.append(choco[i+1])
        else:
            A.append(X)
            X = [choco[i+1]]
    A.append(X)
    white = [0] * (S+1)
    hoge = []
    flag = 1
    for w in range(W): # 一番右側が怖い
        B = [sum([int(A[h][i][w]) for i in range(len(A[h]))]) + white[h] > K for h in range(S+1)]
        if any(B):
            if any([sum([int(A[h][i][w]) for i in range(len(A[h]))]) > K for h in range(S+1)]):
                flag = 0
                break
            cnt += 1
            hoge.append(w-1)
            white = [sum(int(A[h][i][w]) for i in range(len(A[h]))) for h in range(S+1)]
        else:
            for h in range(S+1):
                white[h] += sum(int(A[h][i][w]) for i in range(len(A[h])))
    if flag:
        ans = min(ans, cnt)

print(ans)