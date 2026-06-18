S = input()
n = len(S)
ans = 0

for i in range(n-2):
  for k in range(i+2,n):
    if (k-i) % 2 == 0:
      j = (i+k) // 2
      if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
        ans += 1
print(ans)