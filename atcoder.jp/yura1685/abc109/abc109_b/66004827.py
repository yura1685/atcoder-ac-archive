N = int(input())
W = [input() for _ in range(N)]

for i in range(N-1):
  if W[i][-1] != W[i+1][0]:
    print('No')
    exit()

if len(set(W)) == N:
  print('Yes')
else:
  print('No')