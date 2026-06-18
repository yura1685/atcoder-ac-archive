from collections import Counter

N = int(input())
A = list(map(int,input().split()))
d = Counter(A)

ansM = 0
for v in d.values():
    ansM += v*(v-1)//2

for k in A:
    n = (d[k]-1)
    print(ansM - n)