A, B, C = map(int,input().split())
if A == B == C:
  print('Yes')
else:
  if A+B+C == 2*max(A,B,C):
    print('Yes')
  else:
    print('No')