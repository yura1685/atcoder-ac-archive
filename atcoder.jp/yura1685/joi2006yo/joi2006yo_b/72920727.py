N = int(input())
d = {}
for _ in range(N):
  x = input().split()
  d[x[0]] = x[1]

ans = []
M = int(input())
for _ in range(M):
  y = input()[0]
  if d.get(y) is not None:
    ans.append(d[y])
  else:
    ans.append(y)

print(''.join(ans))