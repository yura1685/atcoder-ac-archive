N, K, Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))
A.append(N+1)

for l in L:
    l -= 1
    if A[l+1] - A[l] > 1:
        A[l] += 1
    else:
        pass
A.pop()
print(*A)