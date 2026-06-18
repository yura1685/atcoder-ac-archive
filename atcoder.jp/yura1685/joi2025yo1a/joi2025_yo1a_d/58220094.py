ans = 0
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(N):
  for j in range(M):
    ans += (A[i] + B[j])*max(A[i],B[j])
print(ans)