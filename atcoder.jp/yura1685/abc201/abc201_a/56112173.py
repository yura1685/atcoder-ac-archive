A, B, C = map(int,input().split())
if A+B==2*C or B+C==2*A or C+A==2*B:
  print('Yes')
else:
  print('No')