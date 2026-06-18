H, W = map(int,input().split())
A = ['']*H
for i in range(H):
    A[i] = list(map(int,input().split()))
Alp = ['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(H):
    for j in range(W):
        A[i][j] = Alp[A[i][j]]
for i in range(H):
    c = ''.join(A[i])
    print(c)