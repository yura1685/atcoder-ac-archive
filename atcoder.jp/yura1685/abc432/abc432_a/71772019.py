from itertools import permutations
X = list(map(int,input().split()))
ans = 0
for a, b, c in permutations(X):
    ans = max(ans, 100*a + 10*b + c)

print(ans)