n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
yummy = max(a)
u = []
for i in range(n):
    if a[i] == yummy:
        u.append(i+1)
for t in u:
    if t in b:
        print('Yes')
        exit()
print('No')