from itertools import accumulate

N = int(input())
S = input()
C = list(map(int,input().split()))

A10 = [C[i] if (S[i] == '0' and i % 2 == 0) or (S[i] == '1' and i % 2 == 1) else 0 for i in range(N)]
A01 = [C[i] if (S[i] == '0' and i % 2 == 1) or (S[i] == '1' and i % 2 == 0) else 0 for i in range(N)]
A10 = list(accumulate(A10))
A01 = list(accumulate(A01))

ans = float('inf')
for i in range(N-1):
    X = A10[i] + A01[-1] - A01[i]
    Y = A01[i] + A10[-1] - A10[i]
    ans = min(ans,X,Y)

print(ans)