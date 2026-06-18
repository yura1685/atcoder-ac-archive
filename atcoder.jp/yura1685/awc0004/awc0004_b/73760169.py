N, T = map(int,input().split())
ans = 0
for _ in range(N):
  a, b= map(int,input().split())
  ans += max(a-b*T, 0)
print(ans)