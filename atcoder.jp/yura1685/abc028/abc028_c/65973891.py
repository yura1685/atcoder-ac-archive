import itertools

A = tuple(map(int,input().split()))

ans = []
x = list(itertools.permutations(A, 3))
for a in x:
    ans.append(sum(a))
ans = list(set(ans));ans.sort()
print(ans[-3])