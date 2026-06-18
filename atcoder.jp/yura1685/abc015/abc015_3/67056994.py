from itertools import product
N, K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]

C = list(product(*T))

for c in C:
    ans = 0
    for x in c:
        ans ^= x
    if ans == 0:
        print('Found')
        exit()
print('Nothing')