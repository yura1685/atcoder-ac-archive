a, b, c = map(int, input().split())
a, b, c = min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c)
if a==b:
  print(c)
elif b==c:
  print(a)
else:
  print(0)