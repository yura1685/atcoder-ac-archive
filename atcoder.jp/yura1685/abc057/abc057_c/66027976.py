def F(A,B):
    n = max(A,B)
    return len(str(n))

N = int(input())
ans = 10**10

for d in range(1,int(N**(0.5)+2)):
    if N % d == 0:
        ans = min(ans, F(d,N//d))

print(ans)