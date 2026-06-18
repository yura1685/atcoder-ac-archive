N = int(input())
man, poi = [], []

for i in range(N):
    S = input()
    point = 0
    for j in range(N):
        if S[j] == 'o':
            point += 1
        elif S[j] == 'x':
            point -= 1
    man.append(i)
    poi.append(point)

L = []

while len(poi) != 0:
    a = max(poi)
    b = poi.index(a)
    L.append(str(man[b]+1))
    man.pop(b)
    poi.pop(b)

print(*L)