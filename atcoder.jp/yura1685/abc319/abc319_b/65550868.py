N = int(input())
S = ''
yakusu = []
for i in range(1,10):
    if N % i == 0:
        yakusu.append(i)

for i in range(N+1):
    s = '-'
    for j in yakusu:
        if i % (N//j) == 0:
            s = str(j)
            break
    S += s
print(S)