N = int(input())
A, B = 0, 0
for _ in range(N):
  a, b = map(int,input().split())
  if a == b:
    A += a
    B += b
  if a < b:
    B += a+b
  if a > b:
    A += a+b

print(A,B)