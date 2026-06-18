N, D, H = map(int,input().split())
height = 0
for i in range(N):
    d, h = map(int,input().split())
    y = (H-h)/(D-d)*(-D)+H
    height = max(height, y)
print(height)