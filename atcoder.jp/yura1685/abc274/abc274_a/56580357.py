a, b = map(int,input().split())
n = str(b/a)
if len(n) <= 5:
    n += '0'*(5-len(n))
    print(n)
    exit()
print(round(float(n),3))