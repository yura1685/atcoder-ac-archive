from itertools import permutations
X = [int(x) for x in input()]
ans = 100000000
for Y in permutations(X):
    if Y[0] == 0:
        continue
    t = 0
    for i in range(len(Y)):
        t += Y[-i-1]*10**i
    ans = min(ans, t)

print(ans)