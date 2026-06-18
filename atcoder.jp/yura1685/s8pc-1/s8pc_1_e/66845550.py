from itertools import accumulate

N, Q = map(int,input().split())
a = list(map(int,input().split()))

road = [pow(a[i],a[i+1],10**9+7) for i in range(N-1)]
road = [0] + list(accumulate(road))

c = [1] + list(map(int,input().split())) + [1,0]

walk = 0

for i in range(Q+1):
    a, b = c[i]-1, c[i+1]-1
    if a > b:
        a, b = b, a
    walk = (walk + road[b] - road[a]) % (10**9+7)

print(walk)