from bisect import bisect

N, M = map(int,input().split())
P = [int(input()) for _ in range(N)] + [0]

twi = set()
for p in P:
    for q in P:
        if p + q <= M:
            twi.add(p+q)
twi = list(twi); twi.sort()

score = 0
for s in twi:
    x = bisect(twi,M-s)
    hoge = s + twi[x-1]
    if hoge > M:
        continue
    score = max(score,hoge)
print(score)