N = int(input())
v = sorted(list(map(int,input().split())))

value = v[0]
for i in v:
    value = (value+i)/2
print(value)