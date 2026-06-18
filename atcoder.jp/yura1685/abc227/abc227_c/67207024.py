N = int(input())
ans = 0

for A in range(1,int(N**(1/3))+10):
    for B in range(A,N+1):
        if A*B*B > N:
            break
        ans += N//(A*B)-B+1
print(ans)