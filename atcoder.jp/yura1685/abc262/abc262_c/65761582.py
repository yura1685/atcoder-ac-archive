N = int(input())
A = list(map(int,input().split()))

equal = 0
swap = 0
for i in range(N):
    if A[i] == i+1:
        equal += 1
    else:
        if A[A[i]-1] == i+1:
            swap += 1
print(equal*(equal-1)//2 + swap//2)