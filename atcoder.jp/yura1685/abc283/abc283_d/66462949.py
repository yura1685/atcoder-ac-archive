s = input()
l = []
p = []
for i in range(len(s)):
  if s[i] == "(":
    l.append(i)
  elif s[i] == ")":
    q = l.pop()
    if q + 1 < i:
      p = p[:q-i+1]
  else:
    if s[i] in p:
      print("No")
      break
    p.append(s[i])
else:
  print("Yes")