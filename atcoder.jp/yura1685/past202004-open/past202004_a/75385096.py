def hoge(X):
    if X[0] == 'B': x = - int(X[1]) + 1
    else: x = int(X[0])
    return x

S, T = input().split()
print(abs(hoge(S) - hoge(T)))