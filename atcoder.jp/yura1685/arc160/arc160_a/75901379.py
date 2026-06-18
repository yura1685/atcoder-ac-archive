N, K = map(int, input().split())
A = [int(n)-1 for n in input().split()]
B = [-1] * N
for i, a in enumerate(A):
    B[a] = i

tento = 0
for L in range(N):
    for R in range(L+1, N):
        if A[R] < A[L]:
            tento += 1

ans = A

if K <= tento:
    flag = False
    for L in range(N):
        if flag: break
        sub = []
        for R in range(L+1, N):
            if A[R] < A[L]:
                sub.append((A[R], R))
        
        pat = len(sub)
        if K <= pat:
            sub.sort()
            _, r = sub[K-1]
            ans = A[:L] + A[L:r+1][::-1] + A[r+1:]
            flag = True
        else:
            K -= pat

elif K <= tento + N:
    ans = A

else:
    K -= (tento + N)
    flag = False
    for L in range(N-1, -1, -1):
        if flag: break
        sub = []
        for R in range(L+1, N):
            if A[R] > A[L]:
                sub.append((A[R], R))
        
        pat = len(sub)
        if K <= pat:
            sub.sort()
            _, r = sub[K-1]
            ans = A[:L] + A[L:r+1][::-1] + A[r+1:]
            flag = True
        else:
            K -= pat

ans = [x+1 for x in ans]
print(*ans)