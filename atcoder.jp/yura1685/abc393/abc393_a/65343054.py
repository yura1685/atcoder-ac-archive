a,b=map(str,input().split())
if a == 'fine':
  print(3 if b == 'sick' else 4)
else:
  print(1 if b == 'sick' else 2)