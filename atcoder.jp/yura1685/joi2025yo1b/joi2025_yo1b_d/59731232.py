N = int(input())
A = list(map(int,input().split()))
while len(A) != 1:
    l = len(A)
    B = []
    for i in range(l-1):
        B.append(A[i] + A[i+1])
    print(*B)
    A = B