N = int(input())
L = [1]*(2*N+1)
for i in range(N):
    L[2*i+1] = 0
L = [str(i) for i in L]
L = ''.join(L)
print(L)