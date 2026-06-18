N = int(input())
c = [None, 10, 9]
c += [9*10**(i//2) for i in range(2,40)]

i = 1
while N - c[i] > 0:
    N -= c[i]
    i += 1

if i == 1:
    exit(print(N-1))

d = (i+1)//2
X = str(N+10**(d-1)-1)

if i % 2 == 1:
    print(X + X[-2::-1])
else:
    print(X + X[::-1])