N = int(input())
if N == 1:
    print(1)
    print(1)
    exit()
c = [2*i for i in range(1,N//2+1)]
print(N//2)
print(*c)