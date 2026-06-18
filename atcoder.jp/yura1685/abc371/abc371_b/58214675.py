N, M = map(int,input().split())
c = [0]*(N+1)
for i in range(M):
  A, B = map(str,input().split())
  A = int(A)
  if B == 'F':
    print('No')
  else:
    if c[A] == 1:
      print('No')
    elif c[A] == 0:
      c[A] += 1
      print('Yes')
