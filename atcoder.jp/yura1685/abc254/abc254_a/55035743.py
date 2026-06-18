N = int(input())
n = str(N % 100)
if len(n) == 1:
  print('0'+n)
else:
   print(n)