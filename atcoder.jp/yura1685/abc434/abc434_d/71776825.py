N = int(input())
cloud = [[0]*2001 for _ in range(2001)]
only = [[0]*2001 for _ in range(2001)]

for i in range(1,N+1):
    U, D, L, R = map(int,input().split())
    U, L = U-1, L-1
    cloud[U][L] += 1
    cloud[U][R] -= 1
    cloud[D][L] -= 1
    cloud[D][R] += 1
    only[U][L] += i
    only[U][R] -= i
    only[D][L] -= i
    only[D][R] += i

for h in range(2001):
    for w in range(1,2001):
        cloud[h][w] += cloud[h][w-1]
        only[h][w] += only[h][w-1]
for w in range(2001):
    for h in range(1,2001):
        cloud[h][w] += cloud[h-1][w]
        only[h][w] += only[h-1][w]

cnt = [0]*(N+1)
sky = 0

for h in range(2000):
    for w in range(2000):
        if cloud[h][w] == 1:
            cnt[only[h][w]] += 1
        elif cloud[h][w] == 0:
            sky += 1

for i in range(1,N+1):
    print(sky + cnt[i])