def f(L):
    return [(j, 3-i) for i, j in L]

P1, P2, P3 = [], [], []

s = []
for i in range(4):
    P = input()
    for j in range(4):
        if P[j] == '#':
            s.append((i, j))
P1.append(s)

s = []
for i in range(4):
    P = input()
    for j in range(4):
        if P[j] == '#':
            s.append((i, j))
P2.append(s)

s = []
for i in range(4):
    P = input()
    for j in range(4):
        if P[j] == '#':
            s.append((i, j))
P3.append(s)

if len(P1[0]) + len(P2[0]) + len(P3[0]) != 16:
    print('No')
    exit()

for _ in range(3):
    P2.append(f(P2[-1]))
    P3.append(f(P3[-1]))

p1 = P1[0]
x1_0, y1_0 = p1[0]

for p2 in P2:
    x2_0, y2_0 = p2[0]
    for p3 in P3:
        x3_0, y3_0 = p3[0]
        for X1 in range(-3, 4):
            for Y1 in range(-3, 4):
                dx1, dy1 = X1-x1_0, Y1-y1_0
                for X2 in range(-3, 4):
                    for Y2 in range(-3, 4):
                        dx2, dy2 = X2-x2_0, Y2-y2_0
                        for X3 in range(-3, 4):
                            for Y3 in range(-3, 4):
                                dx3, dy3 = X3-x3_0, Y3-y3_0
                                s = set()
                                ok = True
                                for (p, dx, dy) in [(p1, dx1, dy1), (p2, dx2, dy2), (p3, dx3, dy3)]:
                                    for x, y in p:
                                        nx, ny = x + dx, y + dy
                                        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in s:
                                            s.add((nx, ny))
                                        else:
                                            ok = False
                                            break
                                    if not ok: break
                                if ok and len(s) == 16:
                                    print('Yes')
                                    exit()

print('No')