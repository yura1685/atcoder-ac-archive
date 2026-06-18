N = int(input())
A = list(map(int,input().split()))
ans = [A[0]]
for i in range(N-1):
    if A[i] < A[i+1]:
        c = [i for i in range(A[i]+1,A[i+1]+1)]
    else:
        c = [i-1 for i in range(A[i+1]+1,A[i]+1)]
        c = sorted(c, reverse = True)
    ans += c
print(*ans)