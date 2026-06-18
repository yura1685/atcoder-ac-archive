n, d = map(int,input().split())
d *= d
point = 0
for i in range(n):
    x, y = map(int,input().split())
    if x**2 + y**2 <= d:
        point += 1
print(point)