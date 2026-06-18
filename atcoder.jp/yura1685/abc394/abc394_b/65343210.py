N = int(input())
c = []
for i in range(N):
  X = input()
  c.append((len(X), X))
c = sorted(c)
ans = ''
for i in range(N):
  ans += c[i][1]
print(ans)