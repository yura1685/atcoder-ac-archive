n = int(input())
d = []
for i in range(n):
  x, y = map(int,input().split())
  d.append([x,y])

for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      x1, y1 = d[i][0], d[i][1]
      x2, y2 = d[j][0], d[j][1]
      x3, y3 = d[k][0], d[k][1]
      if (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) == 0:
        print('Yes')
        exit()
print('No')