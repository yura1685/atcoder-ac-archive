from math import ceil

N = int(input())
A = list(map(int,input().split()))

bug, com = 0, 0

for p in A:
    if p != 0:
        bug += p
        com += 1

print(ceil(bug/com))