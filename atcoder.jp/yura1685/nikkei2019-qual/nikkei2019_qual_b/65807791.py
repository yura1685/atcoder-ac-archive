N = int(input())
A, B, C = list(input()), list(input()), list(input())
x = list(zip(A,B,C))

yura = 0
for i in x:
    yura += len(set(i)) - 1
print(yura)