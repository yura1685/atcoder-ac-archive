N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

ans = 0
for i in range(N):
    candy = sum(A1[:1+i] + A2[i:])
    ans = max(ans, candy)
print(ans)