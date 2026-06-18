N, M = map(int,input().split())
S = input()

Muji = M
Logo = 0
L = []

for j in range(N):
    i = int(S[j])
    if i == 0:
        Muji = M
        Logo = 0
    if i == 1:
        if Muji > 0:
            Muji -= 1
        else:
            Logo -= 1
            L.append(Logo)
    if i == 2:
        Logo -= 1
        L.append(Logo)

print(-min(L) if len(L) > 0 else 0)