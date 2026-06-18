N, R, C = map(int,input().split())
M = input()
s = set([(0,0)])
fire = (0,0)

for m in M:
    if m == 'N':
        fire = (fire[0]+1,fire[1])
        R += 1
    elif m == 'S':
        fire = (fire[0]-1,fire[1])
        R -= 1
    elif m == 'W':
        fire = (fire[0],fire[1]+1)
        C += 1
    else:
        fire = (fire[0],fire[1]-1)
        C -= 1
    s.add(fire)
    print('1' if (R,C) in s else '0', end = '')