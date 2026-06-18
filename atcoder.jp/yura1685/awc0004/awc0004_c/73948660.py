N = int(input())
H = list(map(int, input().split()))
m, M = 0, 0
for h in H:
  m = min(m, h)
  M = max(M, h)
print(2*M - 2*m)