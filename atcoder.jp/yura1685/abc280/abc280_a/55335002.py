H, W = map(int, input(). split())
koma = 0
for i in range(H):
    koma += input().count('#')
print(koma)