N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
S1 = sum(A)

win = 0
for i in range(N):
    if A[i] >= B[i]:
        A[i] -= B[i]
    elif A[i] < B[i]:
        B[i] -= A[i]
        A[i] = 0
        if A[i+1] >= B[i]:
            A[i+1] -= B[i]
        else:
            A[i+1] = 0

S2 = sum(A)
print(S1-S2)