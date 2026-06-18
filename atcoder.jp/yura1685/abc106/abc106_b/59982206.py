N = int(input())
ans = 0
for i in range(N+1):
  if i % 2 == 1:
    pue = 0
    for j in range(1,i+1):
      if i % j == 0:
        pue += 1
    if pue == 8:
      ans += 1
print(ans)