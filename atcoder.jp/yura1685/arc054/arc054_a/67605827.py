L, X, Y, S, D = map(int,input().split())

d1, d2 = (D-S) % L, (S-D) % L

ans = d1/(X+Y)
if X < Y:
    ans = min(ans, d2/(Y-X))

print(ans)