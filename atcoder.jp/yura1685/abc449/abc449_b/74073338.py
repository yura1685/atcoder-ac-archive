H, W, Q = map(int, input().split())

for _ in range(Q):
  q, x = map(int, input().split())
  if q == 1:
    print(x*W)
    H -= x
  else:
    print(x*H)
    W -= x
