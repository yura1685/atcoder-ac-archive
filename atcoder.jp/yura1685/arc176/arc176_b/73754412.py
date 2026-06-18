def solve():
    N, M, K = map(int,input().split())
    if K + 1 == M:
        if N >= K: print(0)
        else: print(pow(2,N,10))
        return 
    V = N % (M - K)
    V += ((M-1) - V) // (M-K) * (M-K)
    if N < M: V = N
    print(pow(2,V,10))

for _ in range(int(input())):
    solve()