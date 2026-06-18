a, b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

pin = '7 8 9 0 4 5 6   2 3     1   '

for x in p:
    pin = pin.replace(str(x),'.')
for y in q:
    pin = pin.replace(str(y),'o')
for i in range(10):
    pin = pin.replace(str(i),'x')

for i in range(4):
    print(pin[7*i:7*i+7])