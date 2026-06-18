from time import time
from random import shuffle

s = time()
N = int(input())
c = [tuple(map(int,input().split())) for _ in range(N)]
d = [[((c[i][0] - c[j][0])**2 + (c[i][1] - c[j][1])**2)**(1/2) for j in range(N)] for i in range(N)]
P = [i for i in range(1,N)]

ans = 10**8
route = []
while True:
    e = time()
    if e - s > 0.9:
        break
    score = 0
    shuffle(P)
    X = [0] + P + [0]
    for i in range(N):
        score += d[X[i]][X[i+1]]
    if score < ans:
        ans = score
        route = X

for x in route:
    print(x+1)