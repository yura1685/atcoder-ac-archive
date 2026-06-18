S = input()
c = [min(3, S.count(str(i))) for i in range(1,10)]
x = []
for i in range(1,10):
    n = c[i-1]
    x += [i for _ in range(n)]

n = len(x)

if n == 1:
    if x[0] % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

elif n == 2:
    if (10*x[0] + x[1]) % 8 == 0 or (10*x[1] + x[0]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

else:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue
                hachi = 100*x[i] + 10*x[j] + x[k]
                if hachi % 8 == 0:
                    print('Yes')
                    exit()
print('No')