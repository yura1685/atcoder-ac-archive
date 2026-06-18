s, t, x = map(int,input().split())
if s == t:
  print('No')
elif s < t:
  if s <= x < t:
    print('Yes')
  else:
    print('No')
else:
  if x < t or s <= x:
    print('Yes')
  else:
    print('No')