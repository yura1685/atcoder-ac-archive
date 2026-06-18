from more_itertools import run_length

N = int(input())
A = list(run_length.encode(map(int, input().split())))
A.reverse()
cnt = [0] * (N+1)
NA = len(A)
L = [0] * (NA + 1)
for i in range(NA):
    a = A[i][1]
    L[i+1] = L[i] + a 

ans = sum(L[:-1]) + 1

for n, c in A:
    ans -= cnt[n]
    cnt[n] += c

print(ans)