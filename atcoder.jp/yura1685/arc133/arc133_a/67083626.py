from more_itertools import run_length

N = int(input())
A = list(map(int,input().split()))
c = list(run_length.encode(A))
n = len(c)

pick = c[-1][0]
for i in range(n-1):
    if c[i][0] > c[i+1][0]:
        pick = c[i][0]
        break

for a in A:
    if a != pick:
        print(a,end=' ')
