A, X, M = map(int,input().split())

def matrix(A, B):
    A00 = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    A01 = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    A10 = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    A11 = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    return [[A00%M, A01%M], [A10%M, A11%M]]

def dfs(A,x,B):
    if x == 0: return B
    if x == 1: return matrix(A, B)
    y, z = x//2, x%2
    if z == 1: B = matrix(A, B)
    A = matrix(A, A)
    return dfs(A, y, B)

print(dfs([[A, 1], [0, 1]], X, [[1,0],[0,1]])[0][1])