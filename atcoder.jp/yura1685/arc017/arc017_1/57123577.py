N = int(input())
for i in range(2,int(N**(1/2))+1):
    if N % i == 0:
        print('NO');exit()
print('YES')