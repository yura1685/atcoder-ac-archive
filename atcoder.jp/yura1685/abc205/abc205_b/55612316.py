N = int(input())
A = list(map(int,input().split()))
for i in range(1,N+1):
    if i not in A:
        print('No')
        exit()
print('Yes')