n, k = map(int,input().split())
light_man = list(map(int,input().split()))
light, dark = [], []


for i in range(1,n+1):
    x, y = map(int,input().split())
    if i in light_man:
        light.append((x,y))
    else:
        dark.append((x,y))

ans = 0
for man in dark:
    man_x, man_y = man
    near = 10**20
    for l in light:
        l_x, l_y = l
        dist = (man_x - l_x)**2 + (man_y - l_y)**2
        near = min(near, dist)
    ans = max(ans, near)
print(ans**(0.5))