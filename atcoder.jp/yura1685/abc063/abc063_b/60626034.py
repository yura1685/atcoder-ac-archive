S = input()
alp = list('abcdefghijklmnopqrstuvwxyz')
for i in S:
  if i not in alp:
    print('no')
    exit()
  else:
    alp.remove(i)
print('yes')