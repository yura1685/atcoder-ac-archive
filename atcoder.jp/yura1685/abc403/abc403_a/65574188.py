N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range((N+1)//2):
  ans += A[2*i]
print(ans)