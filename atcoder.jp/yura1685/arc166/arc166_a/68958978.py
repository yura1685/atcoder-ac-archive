from collections import Counter

def solve(N,X,Y):
    X, Y = list(X), list(Y)
    CX = Counter(X)
    CY = Counter(Y)
    if CX['A'] > CY['A'] or CX['B'] > CY['B']:
        return False
    leftA = CY['A'] - CX['A']
    leftB = CY['B'] - CX['A']
    for i in range(N):
        if leftA == leftB == 0:
            break
        if X[i] == 'C':
            if leftA:
                X[i] = 'A'
                leftA -= 1
            else:
                X[i] = 'B'
                leftB -= 1
    XA = [i for i in range(N) if X[i] == 'A']
    YA = [i for i in range(N) if Y[i] == 'A']
    for i in range(len(XA)):
        if XA[i] > YA[i]:
            return False
    return True

T = int(input())
for _ in range(T):
    N, X, Y = input().split()
    N = int(N)
    ind = [0]
    flag = 0
    for i in range(N):
        if Y[i] == 'C':
            if X[i] != 'C':
                print('No')
                flag = 1
                break
            ind.append(i+1)
    if flag:
        continue
    ind.append(N+1)
    check = []
    for i in range(len(ind)-1):
        if ind[i] + 1 == ind[i+1]:
            continue
        check.append((ind[i+1]-ind[i]-1,X[ind[i]:ind[i+1]-1],Y[ind[i]:ind[i+1]-1]))
    
    print('Yes' if all([solve(n,x,y) for n, x, y in check]) else 'No')