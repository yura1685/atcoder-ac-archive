N = int(input())
A = [0] + list(map(int, input().split()))
ans = []

for i in range(1, N+1):
    x = i
    for j in range(1, 1685):
        x = A[x]
        if x == i:
            ans.append(j)
            break

print(*ans)