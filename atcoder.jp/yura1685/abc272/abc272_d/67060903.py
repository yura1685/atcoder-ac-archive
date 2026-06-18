from collections import deque
from math import isqrt
from itertools import product

N, M = map(int,input().split())
c = set()

for i in range(isqrt(M)+1):
    if isqrt(M-i*i)**2 == M-i*i:
        j = isqrt(M-i*i)
        c |= set(product([i,-i],[j,-j])) | set(product([j,-j],[i,-i]))

glid = [[-1]*N for _ in range(N)]
glid[0][0] = 0

d = deque([(0,0)])

while d:
    h, w = d.popleft()
    for dh, dw in c:
        if 0 <= h+dh < N and 0 <= w+dw < N and glid[h+dh][w+dw] == -1:
            glid[h+dh][w+dw] = glid[h][w] + 1
            d.append((h+dh,w+dw))

for G in glid:
    print(*G)