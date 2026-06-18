s = input()
t = int(input())

unk = 0
x, y = 0, 0

u, d, l, r = s.count('U'), s.count('D'), s.count('L'), s.count('R')
unk = s.count('?')
x = r-l
y = u-d

now = abs(x)+abs(y)
if t == 1:
    print(now+unk)
else:
    if now > unk:
        print(now-unk)
    else:
        if (unk - now) % 2 == 0:
            print(0)
        else:
            print(1)