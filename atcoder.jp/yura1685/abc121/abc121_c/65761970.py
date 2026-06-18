N, M = map(int,input().split())
energy = []
for _ in range(N):
    A, B = map(int,input().split())
    energy.append((A,B))
energy = sorted(energy)

money = 0
buy = 0
shop = 0
while buy < M:
    if buy + energy[shop][1] <= M:
        buy += energy[shop][1]
        money += energy[shop][0] * energy[shop][1]
    else:
        nokori = M - buy
        money += nokori * energy[shop][0]
        buy = M
    shop += 1

print(money)