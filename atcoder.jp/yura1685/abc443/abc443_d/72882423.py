def solve():
    N = int(input())
    R = list(map(int,input().split()))
    S = sum(R)
    for i in range(1,N):
        if R[i] > R[i-1] + 1:
            R[i] = R[i-1] + 1
    for i in range(N-2,-1,-1):
        if R[i] > R[i+1] + 1:
            R[i] = R[i+1] + 1
    print(S - sum(R))


T = int(input())
for _ in range(T):
    solve()