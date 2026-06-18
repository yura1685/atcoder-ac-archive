X, Y = map(int, input().split())
p = [(int(input()), 0) for _ in range(X)]
q = [(int(input()), 1) for _ in range(Y)]
e = sorted(p + q)

ans = 0
tate, yoko = 0, 0
for c, i in e:
    if i == 0:
        ans += c * (Y + 1 - tate)
        yoko += 1
    else:
        ans += c * (X + 1 - yoko)
        tate += 1

print(ans)