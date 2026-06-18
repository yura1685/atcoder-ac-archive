T = int(input())

def solve():
    N = int(input())
    P = [0]+list(map(int,input().split()))
    if P == [i for i in range(N+1)]:
        return 0
    M = 0
    for i in range(1,N+1):
        if P[i] == i and M == i-1:
            return 1
        M = max(M,P[i])
    if P[1] == N and P[-1] == 1:
        return 3
    return 2

for _ in range(T):
    print(solve())