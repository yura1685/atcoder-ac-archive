from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    flag = [1]*(N+1)
    ans = 0
    A = list(map(int,input().split()))
    d = defaultdict(list)
    for i in range(2*N-1):
        if A[i] == A[i+1]:
            flag[A[i]] = 0
            continue
        if d[(min(A[i],A[i+1]), max(A[i],A[i+1]))]:
            n = d[(min(A[i],A[i+1]), max(A[i],A[i+1]))][0]
            if n + 1 == i:
                continue
            if flag[A[i]] and flag[A[i+1]]:
                ans += 1
        else:
            d[(min(A[i],A[i+1]), max(A[i],A[i+1]))].append(i)
    print(ans)