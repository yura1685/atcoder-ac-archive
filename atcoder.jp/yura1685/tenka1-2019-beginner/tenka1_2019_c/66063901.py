from more_itertools import run_length

n = int(input())
s = input()

c = list(run_length.encode(s))
cn = len(c)
ans = 0

if c[0][0] == '.':
    c = c[1:]
    if len(c) == 0:
        print(0)
        exit()

if c[-1][0] == '#':
    c.pop()

black = [i[1] for i in c[::2]]
white = [i[1] for i in c[1::2]]

b, w = 0, sum(white)
ans = b+w

for i in range(len(black)):
    b += black[i]
    w -= white[i]
    ans = min(ans, b+w)

print(ans)