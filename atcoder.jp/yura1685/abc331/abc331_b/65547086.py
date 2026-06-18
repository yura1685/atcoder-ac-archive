N, S, M, L = map(int,input().split())
money = 0
pat = []
for s in range(20):
    for m in range(20):
        for l in range(20):
            if 6*s+8*m+12*l >= N:
                pat.append(s*S+m*M+l*L)
money += min(pat)
print(money)