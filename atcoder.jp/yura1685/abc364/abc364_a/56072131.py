N = int(input())
eat = 0
for i in range(N):
  if input() == 'sweet':
    if eat == 1 and i != N-1:
      print('No')
      exit()
    eat = 1
  else:
    eat = 0
print('Yes')