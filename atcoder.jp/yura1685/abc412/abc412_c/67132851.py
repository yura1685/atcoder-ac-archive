from bisect import *

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    domino = [S[0]]
    X = S[1:N-1]; X.sort()
    X = [S[0]] + X + [S[-1]]
    flag = True
    while 2*domino[-1] < S[-1]:
        c = domino[-1]
        p = X[bisect(X,2*c)-1]
        if domino[-1] == p:
            print(-1)
            flag = False
            break
        else:
            domino.append(p)
    if flag:
        print(len(domino)+1)