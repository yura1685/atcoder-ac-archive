from itertools import permutations, product

N = int(input())
X = ['A','B','C'] + ['.']*(N-3)
X = list(set(permutations(X)))

A, B, C = [], [] ,[]

for x in X:
    for y in x:
        if y == '.':
            continue
        if y == 'A':
            A.append(x)
        elif y == 'B':
            B.append(x)
        elif y == 'C':
            C.append(x)
        break

r = input()
c = input()

D = []
for i in r:
    if i == 'A':
        D.append(A)
    if i == 'B':
        D.append(B)
    if i == 'C':
        D.append(C)

for G in product(*D):
    Z = list(zip(*G))
    if all([(Z[i].count('A') == 1 and Z[i].count('B') == 1 and Z[i].count('C') == 1) for i in range(N)]):
        if all([tuple(['.'])*(Z[i].index(c[i])) == Z[i][:Z[i].index(c[i])] for i in range(N)]):
            print('Yes')
            for i in range(N):
                print(''.join(G[i]))
            exit()

print('No')