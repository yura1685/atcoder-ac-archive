N = int(input())
B = list(map(int,input().split())) + [10**5]
ans = B[0]
for i in range(N-1):
    ans += min(B[i],B[i+1])
print(ans)