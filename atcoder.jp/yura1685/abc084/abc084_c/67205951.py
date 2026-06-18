N = int(input())

train = []
for _ in range(N-1):
    C, S, F = map(int,input().split())
    train.append(S)
    niart = []
    for t in train:
        if t <= S:
            niart.append(S+C)
        else:
            niart.append((t+F-1)//F*F+C)
    train = niart

for t in train:
    print(t)
print(0)