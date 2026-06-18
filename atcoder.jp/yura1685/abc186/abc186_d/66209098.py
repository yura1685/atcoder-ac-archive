N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

def f(n):
    return -2*n+1+N

ans = 0
for a in range(N):
    ans += f(a+1)*A[a]

print(ans)