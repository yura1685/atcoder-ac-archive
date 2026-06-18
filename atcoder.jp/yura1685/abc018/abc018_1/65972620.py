A = int(input())
B = int(input())
C = int(input())

L = [A, B, C]
x = sorted(L, reverse=True)

for i in L:
    print(x.index(i)+1)