alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
ans = 0
for i in range(25):
  a, b = alp[i], alp[i+1]
  ans += abs(s.index(a) - s.index(b))
print(ans)