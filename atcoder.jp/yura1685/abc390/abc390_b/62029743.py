n = int(input())
A = list(map(int,input().split()))
if n == 0:
    print('Yes')
    exit()
for i in range(n-2):
    if A[i]*A[i+2] != A[i+1]**2:
        print('No')
        exit()
print('Yes')