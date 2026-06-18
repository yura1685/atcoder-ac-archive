X, Y, N = map(int, input().split())
L1, L2, L3, L4 = [], [], [] ,[]

def app(x, y, i):
    if y == 0 and 0 <= x < X: L1.append((x, i))
    elif x == X and 0 <= y < Y: L2.append((y, i))
    elif y == Y and 0 < x <= X: L3.append((X-x, i))
    else: L4.append((Y-y, i))

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (0 < x1 < X and 0 < y1 < Y) or (0 < x2 < X and 0 < y2 < Y):
        pass
    else:
        app(x1, y1, i)
        app(x2, y2, i)

L1.sort()
L2.sort()
L3.sort()
L4.sort()

L = [x[1] for x in (L1 + L2 + L3 + L4)]
stack = []
for n in L:
    if stack and stack[-1] == n:
        stack.pop()
    else:
        stack.append(n)

print('NO' if stack else 'YES')