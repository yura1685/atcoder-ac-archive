N = int(input())
S = list(map(int,input().split()))
collect = 0
for i in range(N):
    n = S[i]
    for a in range(1,n//7+2):
        if (n-3*a)%(4*a+3) == 0 and (n-3*a)/(4*a+3) > 0:
            collect += 1
            break
print(N-collect)