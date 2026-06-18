def solve():
  n, k = map(int,input().split())
  if (n,k) == (0,0):
    exit()
  x = list(map(int,input().split()))
  x.sort()
  print(sum(x[:k]))
  
while 1:
  solve()