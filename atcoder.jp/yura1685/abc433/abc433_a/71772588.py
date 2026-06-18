# (x+c) = (y+c)*z
# c = (x-y*z)/(z-1)

x, y, z = map(int,input().split())
u = x - y*z
d = z - 1
print('No' if u % d or u < 0 else 'Yes')