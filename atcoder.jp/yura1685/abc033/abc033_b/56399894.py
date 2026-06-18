N = int(input())
S, P = [], []
for i in range(N):
    s, p = map(str,input().split())
    S.append(s)
    P.append(int(p))

if sum(P) < 2*max(P):
    print(S[P.index(max(P))])
else:
    print('atcoder')