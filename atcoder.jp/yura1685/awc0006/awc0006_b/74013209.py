N, K, T = map(int, input().split())
score = 0
for _ in range(N):
  D, R = map(int, input().split())
  if D * K <= R:
    score += R
print('Yes' if score >= T else 'No')