N = list(map(int, input()))

def good(X):
    if X[0] == 0: return False
    for i in range(len(X)-1):
        if abs(X[i] - X[i+1]) > 1:
            return False
    return True

for i in range(len(N)):
    m = N[i]
    for n in range(10):
        N[i] = n
        if good(N):
            exit(print('Yes'))
    N[i] = m

print('No')