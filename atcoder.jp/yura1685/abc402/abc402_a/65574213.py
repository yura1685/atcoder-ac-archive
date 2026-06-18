S = input()
alp = 'QWERTYUIOPASDFGHJKLZXCVBNM'
ans = ''
for i in S:
  if i in alp:
    ans += i
print(ans)