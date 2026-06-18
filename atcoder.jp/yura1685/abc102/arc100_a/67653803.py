from statistics import median_low

N = int(input())
A = input().split()
A = [int(A[i])-i for i in range(N)]
med = median_low(A)
ans = sum(abs(a-med) for a in A)
print(ans)