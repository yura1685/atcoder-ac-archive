N = int(input())
A = map(int,input().split())
ans = 0
for num in A:
  a = 0
  while num % 2 == 0:
    num //= 2
    a += 1
  ans += a
print(ans)