def solve():
    a1, a2, a3, a4, a5 = map(int, input().split())
    p1, p2, p3, p4, p5 = map(int, input().split())
    p = 1*a1 + 2*a2 + 3*a3 + 4*a4 + 5*a5
    q = a1 + a2 + a3 + a4 + a5
    N = 3*q - p
    if N <= 0: print(0); return
    ans = 10 ** 19
    ans = min(ans, N * p4)
    ans = min(ans, p4 + N // 2 * p5)
    ans = min(ans, (N+1) // 2 * p5)
    print(ans)

for _ in range(int(input())):
    solve()