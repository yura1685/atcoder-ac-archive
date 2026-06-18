N = int(input())
Pxy, Px, Py = [], set(), set()

for _ in range(N):
    x, y = map(int,input().split())
    Pxy.append((x+y,x-y))
    Px.add(x+y)
    Py.add(x-y)

Mx, mx = max(Px), min(Px)
My, my = max(Py), min(Py)

d = (max(Mx-mx, My-my)+1)//2

L = [(mx+d,my+d), (mx+d,My-d), (Mx-d, my+d), (Mx-d, My-d)]

for p, q in L:
    if (p+q) % 2 == 1:
        continue
    if len(set(max(abs(p-x), abs(q-y)) for x, y in Pxy)) == 1:
        exit(print((p+q)//2, (p-q)//2))