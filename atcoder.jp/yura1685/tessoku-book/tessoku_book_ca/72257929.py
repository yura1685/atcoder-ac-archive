a, b = map(int,input().split())
for n in range(a, b+1):
  if 100 % n == 0:
    exit(print('Yes'))

print('No')