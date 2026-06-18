from itertools import product

N = list(input())
N.sort(reverse=True)

n = len(N)
c = list(product([0,1], repeat=n))

ans = 0
for i in c:
    a, b = '', ''
    for j in range(n):
        if i[j] == 0:
            a += N[j]
        else:
            b += N[j]
    if a and b:
        ans = max(ans, int(a)*int(b))

print(ans)