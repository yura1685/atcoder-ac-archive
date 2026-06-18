from itertools import accumulate

N, W = map(int,input().split())

water = [0]*(201685)
for _ in range(N):
    s, t, p = map(int,input().split())
    water[s] += p
    water[t] -= p

hoge = accumulate(water)
if max(hoge) <= W:
    print('Yes')
else:
    print('No')