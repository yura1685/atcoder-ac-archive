N = int(input())
A = list(map(int,input().split()))
if 0 in A:
    print(0);exit()
pi = 1
count = 0
while pi <= 10**18:
    if count == N:
        print(pi);exit()
    pi *= A[count]
    count += 1
print(-1)