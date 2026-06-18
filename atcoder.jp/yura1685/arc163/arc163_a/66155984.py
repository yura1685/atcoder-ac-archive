T = int(input())
for _ in range(T):
  N = int(input())
  S = input()
  flag = 1
  for i in range(1,N):
    if S[:i] < S[i:]:
      print('Yes')
      flag = 0
      break
  if flag:  
    print('No')