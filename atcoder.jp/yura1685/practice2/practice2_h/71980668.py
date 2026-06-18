from atcoder.twosat import TwoSAT

N, D = map(int,input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int,input().split())
    X.append(x)
    Y.append(y)

twosat = TwoSAT(N)

for i in range(N-1):
    for j in range(i+1,N):
        if abs(X[i] - X[j]) < D:
            twosat.add_clause(i, False, j, False)
        if abs(X[i] - Y[j]) < D:
            twosat.add_clause(i, False, j, True)
        if abs(Y[i] - X[j]) < D:
            twosat.add_clause(i, True, j, False)
        if abs(Y[i] - Y[j]) < D:
            twosat.add_clause(i, True, j, True)

if not twosat.satisfiable():
    print('No')

else:
    print('Yes')
    ans = twosat.answer()
    for i, bool in enumerate(ans):
        print((X if bool else Y)[i])