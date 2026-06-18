N, M = map(int,input().split())

Lm = 0
Rm = 10**5

for _ in range(M):
    l, r = map(int,input().split())
    Lm = max(Lm, l)
    Rm = min(Rm, r)

print(max(Rm-Lm+1, 0))