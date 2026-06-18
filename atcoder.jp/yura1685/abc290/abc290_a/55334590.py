N, M = map(int, input(). split())
Point = list(map(int, input(). split()))
Solve = list(map(int, input(). split()))
p = 0
for i in range(M):
    p += Point[Solve[i]-1]
print(p)