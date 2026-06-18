H, A = map(int,input().split())
attack = 0
while A*attack < H:
    attack += 1
print(attack)