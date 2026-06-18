S = input()
n = len(S)
ans = ''
for i in range(n):
  if S[i] != '.':
    ans += S[i]
print(ans)