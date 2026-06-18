N = int(input())
a, b = map(str,input().split())
c, d = map(str,input().split())
if b < d:
    mount1, mount2 = int(d), int(b)
    name1, name2 = c, a
else:
    mount1, mount2 = int(b), int(d)
    name1, name2 = a, c
for i in range(N-2):
    S, T = map(str,input().split())
    T = int(T)
    if mount2 < T < mount1:
        mount2 = T
        name2 = S
    elif mount1 < T:
        mount1, mount2 = T, mount1
        name1, name2 = S, name1
print(name2)