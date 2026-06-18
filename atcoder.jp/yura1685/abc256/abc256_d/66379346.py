from itertools import accumulate
from more_itertools import run_length

N = int(input())

x = [0]*(200002)
for _ in range(N):
    L, R = map(int,input().split())
    x[L] += 1
    x[R] -= 1
x = list(accumulate(x))
for i in range(200002):
    if x[i] > 0:
        x[i] = 1

run = list(run_length.encode(x))

ans = 0
for i in range(len(run)-1):
    hoge = run[i]
    if i == 0:
        ans += hoge[1]
        print(ans,end=' ')
    elif hoge[0] == 0 and i != 0:
        ans += hoge[1]
        print(ans,end=' ')
    else:
        ans += hoge[1]
        print(ans)