X = int(input())
ans = 0
for i in range(1,10):
  for j in range(1,10):
    if i*j == X:
      ans += 1
print(2025-ans*X)