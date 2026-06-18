N = int(input())
flav = []
for _ in range(N):
    F, S = map(int,input().split())
    flav.append((S,F))

flav.sort(reverse=True)

ice = []
for i in range(N):
    F, S = flav[i]
    if i == 0:
        ice.append(F)
        aji = S
    elif S == aji:
        ice.append(F//2)
    else:
        ice.append(F)
ice.sort(reverse=True)
print(ice[0]+ice[1])