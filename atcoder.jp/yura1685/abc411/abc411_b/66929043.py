N = int(input())
D = list(map(int,input().split()))

for i in range(N-1):
    ans = []
    for j in range(i+1,N):
        ans.append(sum(D[i:j]))
    print(*ans)