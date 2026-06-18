A, B, T = map(int,input().split())
counter = 0
Biscuit = []
for t in range(1,T+1):
    if t % A == 0:
        counter += B
    Biscuit.append(counter)
print(Biscuit[T-1])