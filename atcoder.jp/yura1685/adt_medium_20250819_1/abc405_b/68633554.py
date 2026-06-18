N, M = map(int,input().split())
A = list(map(int,input().split()))
L = [0]*(M+1)
for a in A:
  L[a] += 1
  
if min(L[1:]) == 0:
  exit(print(0))
  
for i in range(N):
  a = A.pop()
  L[a] -= 1
  if not L[a]:
    exit(print(i+1))