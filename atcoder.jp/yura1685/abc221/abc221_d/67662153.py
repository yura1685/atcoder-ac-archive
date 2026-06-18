from collections import defaultdict
from sortedcontainers import SortedSet

N = int(input())
d = defaultdict(int)
D = SortedSet()
for _ in range(N):
    A, B = map(int,input().split())
    d[A] += 1
    d[A+B] -= 1
    D.add(A)
    D.add(A+B)

login = [0]*(N+1)
man = 0
l = len(D)

for i in range(l-1):
    day = D[i]
    man += d[day]
    X = D[i+1]
    login[man] += D[i+1]-D[i]

print(*login[1:])