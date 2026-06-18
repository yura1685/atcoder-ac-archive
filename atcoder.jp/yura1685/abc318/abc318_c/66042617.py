from more_itertools import batched

N, D, P = map(int,input().split())
f = list(map(int,input().split()))
f.sort(reverse=True)
L = list(batched(f,D))

money = 0
for i in L:
    money += min(P,sum(i))

print(money)