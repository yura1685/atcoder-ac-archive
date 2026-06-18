K, N = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(A[i]-A[i-1])
B[0] += K
print(sum(B)-max(B))