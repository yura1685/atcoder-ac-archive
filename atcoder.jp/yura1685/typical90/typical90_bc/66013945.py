from itertools import combinations

N, P, Q = map(int,input().split())
A = list(map(int,input().split()))
A = [x % P for x in A]
ans = 0
for x in combinations(A,5):
    s = 1
    for t in x:
        s = (s*t)%P
    if s == Q:
        ans += 1

print(ans)