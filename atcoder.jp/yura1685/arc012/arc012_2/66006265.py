N, va, vb, L = map(int,input().split())

d = L
for _ in range(N):
    time = d / va
    d += time*(vb-va)

print(d)