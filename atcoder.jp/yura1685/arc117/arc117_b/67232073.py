N = int(input())
A = list(map(int,input().split()))
A.sort(); A = [0] + A
mod = 10**9 + 7

B = [A[i+1]-A[i]+1 for i in range(N)]
ans = 1
for b in B:
    ans = (ans*b)%mod

print(ans)