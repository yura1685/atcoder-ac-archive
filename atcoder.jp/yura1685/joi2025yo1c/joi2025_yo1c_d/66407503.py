N = int(input())
S = input()

P = []
for i in range(1,N):
    if N % i == 0:
        P.append(i)

for p in P:
    Sp = S[:p]
    if Sp*(N//p) == S:
        print('Yes')
        exit()
print('No')