N = int(input())
A = [''] * N
B = [''] * N
for i in range(N):
    A[i] = input()
for i in range(N):
    B[i] = input()
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i+1,j+1)
            exit()