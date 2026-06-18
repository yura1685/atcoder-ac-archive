n, p, q, r, s = map(int,input().split())
A = list(map(int,input().split()))
B = A[:p-1] + A[r-1:s] + A[q:r-1] + A[p-1:q] + A[s:]
print(*B)