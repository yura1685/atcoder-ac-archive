def solve():
    N = int(input())
    P = [int(x) - 1 for x in input().split()]

    ans = N
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                ans -= 1
                break
    print(ans)

for _ in range(int(input())):
    solve()