H, W = map(int,input().split())
A = ['']*H
for i in range(H):
    A[i] = list(map(int,input().split()))
a = 100
for j in range(H):
    a = min(a,min(A[j]))
ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j] - a
print(ans)