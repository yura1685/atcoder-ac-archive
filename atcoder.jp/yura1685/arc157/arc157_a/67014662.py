l = list(map(int, input().split()))
a, b = l[2], l[3]
if a == b == 0:
  if l[1]*l[4] > 0:
    print('No')
    exit()
print('Yes' if abs(l[2]-l[3]) < 2 else 'No')