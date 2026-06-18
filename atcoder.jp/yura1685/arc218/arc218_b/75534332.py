from more_itertools import run_length

def f(L: list) -> bool:
    N = len(L)
    dp = [False] * N
    for i in range(N):
        if i == 0: dp[i] = True
        elif L[i] == 1: dp[i] = not dp[i-1]
        else: dp[i] = True
    return dp[-1]

def solve():
    _ = int(input())
    A = list(run_length.encode(sorted(map(int, input().split()))))

    X = []

    if A[0][0] > 0:
        X.append(A[0][0])

    for i in range(len(A)):
        a = A[i][1]
        X.append(a)
        if i + 1 < len(A):
            a = A[i+1][0] - A[i][0]
            X.append(a)
            
    X.reverse()
    print('Alice' if f(X) else 'Bob')

for _ in range(int(input())):
    solve()