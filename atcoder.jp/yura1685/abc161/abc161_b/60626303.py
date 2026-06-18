N, M = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)
chose = 0
border = S/(4*M)
for i in A:
  if i >= border:
    chose += 1
if chose >= M:
  print('Yes')
else:
  print('No')