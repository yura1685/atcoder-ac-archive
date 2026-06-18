n = int(input())
ans = 1
while 2**ans <= n:
  ans += 1
print(2**(ans-1))