N = int(input())
otosidama = 0
for i in range(N):
    x, u = map(str,input().split())
    if u == 'JPY':
        otosidama += float(x)
    else:
        otosidama += 380000*float(x)
print(otosidama)