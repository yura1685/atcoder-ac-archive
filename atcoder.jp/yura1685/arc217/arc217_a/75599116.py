L = list(range(1,200001))
for i in range(2, 200001, 4):
    L[i-1], L[i] = L[i], L[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    ans = L[:N]
    if N % 4 == 2:
        ans.pop()
        ans.append(N)
    print(*ans)