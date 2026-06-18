L = list(map(int,input().split()))
L.sort()
a, b, c = L[0], L[1], L[2]
x = c-a
y = c-b
if c-x-y < 0:
    print(-1)
else:
    print(c)