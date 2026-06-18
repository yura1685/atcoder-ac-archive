a, b = map(str,input().split())
n = int(a+b)
for i in range(401):
    if i**2 == n:
        print('Yes')
        exit()
print('No')