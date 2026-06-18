from itertools import product

N, M, K = map(int,input().split())
test = []
for _ in range(M):
    X = input().split()
    Y = [X[-1]]
    for i in range(int(X[0])+1):
        Y.append(int(X[i])) # type: ignore
    test.append(Y)

ans = 0
for P in product((0,1),repeat=N): # 1が正しい鍵
    flag = True
    for case in test:
        c = 0
        cor = True if case[0] == 'o' else False # ドアが開いたか否か 
        for i in range(2,2+int(case[1])):
            c += P[case[i]-1] # 差し込んだ正しい鍵の数
        if (c < K and cor) or (c >= K and not cor):
            flag = False
            break
    if not flag:
        continue
    else:
        ans += 1

print(ans)