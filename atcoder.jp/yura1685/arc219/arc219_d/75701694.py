def solve():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    xor = 0
    for i in range(N):
        for j in range(N):
            if i == j == 0: continue
            if (i + j) % 2: xor ^= A[i][j] % (K+1)
    print('Alice' if xor else 'Bob')

for _ in range(int(input())):
    solve()