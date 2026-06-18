N, M = map(int,input().split())
A = list(map(int,input().split()))
print(N-M)
c = []
for i in range(1,N+1):
  if i not in A:
    c.append(i)
print(*c)