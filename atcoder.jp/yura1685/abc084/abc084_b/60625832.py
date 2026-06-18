a, b = map(int,input().split())
bango = input()
num = '1234567890'
for i in range(a+b+1):
  if i != a:
    if bango[i] not in num:
      print('No')
      exit()
  else:
    if bango[i] != '-':
      print('No')
      exit()
print('Yes')