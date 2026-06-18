a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
a3, b3 = map(int,input().split())

c = [a1,a2,a3,b1,b2,b3]

hoge = 0
for i in c:
    if c.count(i) % 2 == 1:
        hoge += 1
if hoge in [0,2]:
    print('YES')
else:
    print('NO')