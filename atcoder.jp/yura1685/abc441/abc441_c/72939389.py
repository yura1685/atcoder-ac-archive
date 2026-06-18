N, K, X = map(int,input().split())
A = sorted(map(int,input().split()))

sake = A[:K]

if sum(sake) < X: exit(print(-1))

ans = N - K
drink = 0
while drink < X:
    a = sake.pop()
    drink += a 
    ans += 1

print(ans)