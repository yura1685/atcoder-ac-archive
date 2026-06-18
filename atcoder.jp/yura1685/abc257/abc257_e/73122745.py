N = int(input())
C = [N+1] + list(map(int,input().split()))
m = min(C)
for n in range(9,-1,-1):
    if C[n] == m:
        i = n 
        break
L = N // m
A = {i: L}
C = [c-m for c in C][i+1:]
N -= L * m

n = 9
while C and N > 0:
    cost = C[-1]
    A[i] -= N // cost
    A[n]  = N // cost
    N %= cost
    n -= 1
    C.pop()

ans = [str(a) * A[a] for a in A]
ans.sort(reverse=True)

print(''.join(ans))