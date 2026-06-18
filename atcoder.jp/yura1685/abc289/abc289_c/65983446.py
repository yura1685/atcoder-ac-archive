from itertools import product

N, M = map(int,input().split())
arr = list(product([0,1], repeat=M))
A = ['']*M


for i in range(M):
    C = int(input())
    a = set(map(int,input().split()))
    A[i] = a # type: ignore

ans = 0
for i in arr:
    x = set()
    for j in range(M):
        if i[j] == 1:
            x |= A[j] # type: ignore
    if x == {m for m in range(1,N+1)}:
        ans += 1
print(ans)