from itertools import permutations

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
r = 0
for i, j, k in permutations([4,5,6]):
    r += A.count(i) * B.count(j) * C.count(k)
print(r / 216)