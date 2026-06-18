def solve():
    N = int(input())
    A = list(map(int,input().split()))
    S = sum(A)
    p, q = S // N, S % N
    B = [p] * N
    for i in range(q):
        B[-1-i] += 1
    flag = True
    for i in range(N-1):
        if A[i] > B[i]:
            flag = False
            break
        else:
            r = B[i] - A[i]
            A[i] += r
            A[i+1] -= r
    print('Yes' if flag else 'No')

t = int(input())
for _ in range(t):
    solve()