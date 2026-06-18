N, M = map(int,input().split())
ans = 0
for _ in range(N):
  a, b = map(int,input().split())
  ans = max(ans, (M-a+b-1)//b)
print(ans)