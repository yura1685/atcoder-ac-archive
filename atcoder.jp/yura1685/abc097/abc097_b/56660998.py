from collections import Counter
import math

X = int(input())
while True:
    p = X
    L = []
    a = 2
    while p != 1:
        if p % a == 0:
            p = p//a
            L.append(a)
        else:
            a += 1
    c = Counter(L)
    u = []
    for i in c:
        u.append(c[i])
    if math.gcd(*u) != 1:
        print(X);exit()
    X -= 1