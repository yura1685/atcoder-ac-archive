from itertools import accumulate

T = int(input())
N = int(input())

shift = [0]*(T+1)
for _ in range(N):
    L, R = map(int,input().split())
    shift[L] += 1
    shift[R] -= 1

shift = list(accumulate(shift))

for i in range(T):
    print(shift[i])