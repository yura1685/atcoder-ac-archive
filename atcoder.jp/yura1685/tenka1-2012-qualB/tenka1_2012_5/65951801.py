a, b, c = map(int,input().split())
for n in range(1,128):
  if n % 3 == a and n % 5 == b and n % 7 == c:
    print(n)