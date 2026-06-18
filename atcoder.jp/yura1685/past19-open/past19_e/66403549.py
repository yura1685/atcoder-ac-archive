n = int(input())
s = input()
S = []
cnt = 0
flag = False
i = 0
while i<n:
  if not flag and i<n-1 and s[i]=='/' and s[i+1]=='*':
    S.append(s[i])
    S.append(s[i+1])
    k = i
    flag = True
    i += 2
  elif flag  and i<n-1 and s[i]=='*' and s[i+1]=='/':
    for _ in range(i-k):S.pop()
    flag = False
    i += 2
  else:
    S.append(s[i])
    i += 1
print("".join(S))